import random 
from Monster.Monsters import monsters
from Skills.Skills_list import Skill_type
from Game.Choices_func import make_query, choose_targets
from collections import deque 
import time

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
        self.order_queue = deque()
        for i in range(random.randint(1, self.max_enemies)):
            monster_key = random.choice(list(monsters.keys()))
            self.enemies_lst.append(monsters[monster_key]())

    def begin_encounter(self, players): 
        # print(self.description) #TODO descriptions
        flag = 0
        while flag==0: 
            self.calculate_turn_order(players)
            while self.order_queue:
                time.sleep(1)
                obj = self.order_queue.popleft()

                if obj.hostile == True:
                    self.hostile_decision(obj, players)
                else:
                    self.player_decision(obj)
                if self.check_combat_status(players):
                    flag = 1
                    break
    
    def player_decision(self, player): #TODO player status
        print(f"\n{player.name} turn")
        skills = player.check_skills()
        ability = make_query("Choose ability", skills)
        while ability == None:
            print("You do not have enough MP for this skill!")
            ability = make_query("Choose ability", skills)

        damage_multiplayers = player.get_damage_multiplayers()
        
        if ability.skill_type == Skill_type.SINGLE_TARGET: 
            target = make_query("Which enemy you wish to attack?", self.enemies_lst) 
            ability.func(damage_multiplayers, target)
        elif ability.skill_type == Skill_type.AOE: 
            targets = choose_targets(self.enemies_lst, ability.n_targets)
            ability.func(damage_multiplayers, targets)
        elif ability.skill_type == Skill_type.SELF_CAST:
            ability.func(damage_multiplayers, player)

        player.mana_points -= ability.cost
        if target.health_points <= 0:
            print(f"{target.name} died")
            self.enemies_lst.remove(target)

    def hostile_decision(self, monster, players): #TODO More advance monster attack - maybe based on simple ML model
        print(f"\n{monster.name} turn")

        target = random.choice(players)
        ability = random.choice(monster.check_skills())
        ability = ability["value"]

        damage_multiplayers = monster.get_damage_multiplayers()
        ability.func(damage_multiplayers, target)
        print(f"{monster.name} attacked {target.name} with {ability.name}!")
        if target.health_points <= 0:
            print(f"{target.name} died")
            players.remove(target)
    
    def calculate_turn_order(self, players):
        self.order_queue.clear()
        objects_sorted = players + self.enemies_lst
        objects_sorted.sort(key=lambda x: x.speed)
        for obj in objects_sorted:
            self.order_queue.append(obj)

    def check_combat_status(self, players):   
        if not players:
            print("You lost because your team died")
            return True
        elif not self.enemies_lst:
            print("You won by defeating all opponents")
            return True
        else:
            return False


    class Safe_encounter(Encounter): #TODO safe encouner
        pass