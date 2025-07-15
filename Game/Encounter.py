import random 
from Game.Encounter_desc import generate_encounter_desc
from Monster.Monsters import monsters
from Skills.Skills_list import Skill_type
from Game.Choices_func import make_query, choose_targets, show_message
from collections import deque 
import time

class Encounter:
    def __init__(self,  players, hostile):
        self.description = generate_encounter_desc(hostile)
        self.players = players

    def begin_encounter(self):
        pass

    def decision(self):
        pass

    def check_status(self):
        pass
    
    def generate_desc(self):
        pass

class HostileEncounter(Encounter): 
    def __init__(self, players, max_enemies):
        super().__init__(players, hostile=True)
        self.max_enemies = max_enemies
        self.enemies_lst = []
        self.order_queue = deque()
        for i in range(random.randint(1, self.max_enemies)):
            monster_key = random.choice(list(monsters.keys()))
            self.enemies_lst.append(monsters[monster_key]())
        
        self.description += f"\nYour team encounter {self.enemies_lst}" #TODO better encounter status message

    def begin_encounter(self):  #TODO print player status
        show_message(self.description)
        flag = 0
        i = 1
        while flag==0:
            self.calculate_turn_order()
            print(f"\nRound {i}\nCurrent turn order {[(i+1, self.order_queue[i]) for i in range(len(self.order_queue))]}") #TODO better turn message
            while self.order_queue:
                time.sleep(1)
                self.execute_turn()
                if self.check_combat_status(self.players):
                    flag = 1
                    break
            i += 1

    def calculate_turn_order(self):
        self.order_queue.clear()
        objects_sorted = self.players + self.enemies_lst
        objects_sorted.sort(key=lambda x: x.speed)
        for obj in objects_sorted:
            self.order_queue.append(obj)
        self.order_queue.reverse()

    def execute_turn(self):
        obj = self.order_queue.popleft()
        print(f"\n{obj.name} turn")
        if obj.hostile:
            self.hostile_decision(obj) 
        else:
            self.player_decision(obj)

    def player_decision(self, player):
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
            target = player
            ability.func(damage_multiplayers, target)

        player.mana_points -= ability.cost
        self.check_if_dead(target)

    def hostile_decision(self, monster): #TODO More advance monster attack - maybe based on simple ML model
        target = random.choice(self.players)
        ability = random.choice(monster.check_skills())
        ability = ability["value"]
        damage_multiplayers = monster.get_damage_multiplayers()

        ability.func(damage_multiplayers, target)
        print(f"{monster.name} attacked {target.name} with {ability.name}!")
        self.check_if_dead(target)

    def check_if_dead(self, target):
        if target.health_points <= 0:
            print(f"{target.name} died")
            self.enemies_lst.remove(target) if target.hostile else self.players.remove(target)

    def check_combat_status(self, players):   
        if not players:
            print("You lost because your team died")
            return True
        elif not self.enemies_lst:
            print("You won by defeating all opponents")
            return True
        else:
            return False
        

    class SafeEncounter(Encounter): #TODO safe encouner
        pass