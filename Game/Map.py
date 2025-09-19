from Game.Encounter.Encounter import HostileEncounter, SafeEncounter, BossEncounter
from PlayerClasses.Inventory.item_generator import Item_generator
import random

class Map:
    def __init__(self, players, difficulty_key, max_steps=3, safe_zones_number = 0, max_enemies = 3, boss=False):
        #Map specifications
        self.max_steps = max_steps
        self.safe_zones = []
        self.safe_zones_number = safe_zones_number
        self.max_enemies = max_enemies
        self.boss = boss
        self.current_encounter = None
        
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
    
    def generate_rooms(self):
        self.generate_safezones() #TODO rework safeencounter to new game idea
        self.rooms_dict = {}
        for i in range(self.max_steps):
            self.rooms_dict[i+1] = HostileEncounter if i+1 not in self.safe_zones else SafeEncounter
        if self.boss:
            self.rooms_dict["Boss"] = BossEncounter

    def begin_adventure(self): 
        self.generate_rooms()
        for key in self.rooms_dict:
            if self.players:
                self.current_encounter = self.rooms_dict[key](self.players, max_enemies=self.max_enemies, room_number=key, team_level=self.team_level) 
                self.current_encounter.begin_encounter()
                self.generate_rewards()
            else:
                return None
        self.succes_flag = True
    
    def generate_rewards(self): #TODO message about loot found
        #Gold
        base_gold = 150
        self.rewards["gold"] += int(base_gold * (self.team_level ** 1.2) * random.uniform(0.8, 1.2))
        #Item
        ticket = random.random()
        self.rewards["items"].append(self.item_generator.generate_item(difficulty_key=self.difficulty_key, level=self.team_level)) if ticket > 0.5 else None
        #Exp
        base_exp = 50
        self.rewards["exp"] += int(base_exp * self.current_encounter.n_enemies * (self.team_level ** 1.2)) #we use team_level because monster levels are based on team level

    def grant_rewards(self):
        self.players.stash.wallet.earn(self.rewards["gold"])
        for item in self.rewards["items"]:
            self.players.stash.add_item(item)
        for player in self.players.get_team_members():
            player.gain_exp(self.rewards["exp"])
    
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__