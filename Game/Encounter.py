import random 
from InquirerPy import inquirer
from Monster.Monsters import monsters
from Skills.Skills_list import Skill_type

def make_query(message, choices):
    choice = inquirer.select(
            message=message,
            choices= choices,
        ).execute()
    return choice 

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
        print(self.description)
        while self.check_status(player):
            self.decision(player)
    
    def decision(self, player): #TODO player status/monster attack
        ability = make_query("Choose ability", player.skills)
        if ability.skill_type == Skill_type.SINGLE_TARGET:  
            target = make_query("Which enemy you wish to attack?", self.enemies_lst)
            ability.func(target, player.ability_power)
        else: #TODO ability usages in difrent ability types
            pass
    
    def check_status(self, player): #TODO safe encouner
        if player.health_points <= 0 or self.enemies_lst[0].health_points <= 0:
            return False
        else:
            return True
        
        
        