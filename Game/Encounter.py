import random 
from rich import console
from Monster.Monsters import monsters
from Skills.Skills_list import Skill_type
from Game.Choices_func import make_query, choose_targets

class Encounter:
    def __init__(self, desc):
        self.description = desc

    def begin_encounter(self):
        pass

    def decision(self):
        pass

    def check_status(self):
        pass

class Hostile_encounter(Encounter):
    def __init__(self, desc, max_enemies):
        super().__init__(desc)
        self.max_enemies = max_enemies
        self.enemies_lst = []
        for i in range(random.randint(1, self.max_enemies)):
            monster_key = random.choice(list(monsters.keys()))
            self.enemies_lst.append(monsters[monster_key]())

    def begin_encounter(self, player):
        print(self.description) #TODO descriptions
        while self.check_status(player):
            self.decision(player)
    
    def decision(self, player): #TODO player status/monster attack / ability usages in difrent ability types
        print(f"{player.name} turn")
        ability = make_query("Choose ability", player.skills)
        damage_multiplayers = player.get_damage_multiplayers()
        
        if ability.skill_type == Skill_type.SINGLE_TARGET:  
            target = make_query("Which enemy you wish to attack?", self.enemies_lst) #TODO mechanism of mana calcualtion and checking if enough
            ability.func(damage_multiplayers, target)
            player.mana_points -= ability.cost
        elif ability.skill_type == Skill_type.AOE: 
            targets = choose_targets(self.enemies_lst, ability.n_targets)
            ability.func(damage_multiplayers, targets)
            player.mana_points -= ability.cost

    def check_status(self, player): 
        if player.health_points <= 0 or self.enemies_lst[0].health_points <= 0:
            return False
        else:
            return True
        
        
    #TODO safe encouner