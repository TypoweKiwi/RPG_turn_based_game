from Game.Encounter.Encounter import HostileEncounter, SafeEncounter
from PlayerClasses.Inventory.item_generator import Item_generator
import random

class Map:
    def __init__(self, players, difficulty_key, max_steps=3, safe_zones_number = 0, max_enemies = 3, boss=False):
        #Map specifications
        self.max_steps = max_steps
        self.current_position = 0
        self.safe_zones = []
        self.safe_zones_number = safe_zones_number
        self.max_enemies = max_enemies
        self.boss = boss
        
        #Team
        self.players = players

        #Rewards and difficulty
        self.succes_flag = False
        self.team_level = self.players.get_team_level()
        self.difficulty_key = difficulty_key
        self.item_generator = Item_generator()
        self.rewards = {
            "gold": 0,
            "items": [],
            "exp": 0
        }

    def generate_safezones(self):
        self.safe_zones = random.sample(range(1, self.max_steps+1), self.safe_zones_number)

    def generate_encounter(self, step): #TODO rework safeencounter to new game idea
        if step not in self.safe_zones:
            self.current_encounter = HostileEncounter(self.players, max_enemies=self.max_enemies, room_number=step, team_level=self.team_level)
        else:
            self.current_encounter = SafeEncounter(self.players, room_number=step)
    
    def generate_boss_encounter(self): #TODO generate boss encounter 
        pass
    
    def begin_adventure(self):
        self.generate_safezones()
        for step in range(self.max_steps):
            if self.players:
                self.generate_encounter(step+1)
                self.current_encounter.begin_encounter()
                self.generate_rewards()
            else:
                return None
        if self.boss:
            self.generate_boss_encounter()
            self.current_encounter.begin_encounter()
        self.succes_flag = True
    
    def generate_rewards(self): #TODO message about loot found
        #Gold
        base_gold = 150
        self.rewards["gold"] += int(base_gold * (self.team_level ** 1.2) * random.uniform(0.8, 1.2))

        #Item
        ticket = random.random()
        self.rewards["items"].append(self.item_generator.generate_item(difficulty_key=self.difficulty_key, level=self.team_level)) if ticket > 0.3 else None

        #Exp
        base_exp = 100
        self.rewards["exp"] += int(base_exp * self.current_encounter.n_enemies (self.team_level ** 1.2))

    def grant_rewards(self): #TODO adding to stash finded items and gold
        pass
    
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__