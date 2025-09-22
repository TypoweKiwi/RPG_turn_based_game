from Game.Encounter.Encounter import HostileEncounter, SafeEncounter, BossEncounter
from Game.UI.Choices_func import show_message
from PlayerClasses.Inventory.item_generator import Item_generator
import random

class Map:
    def __init__(self, team, difficulty_key, max_steps=3, safe_zones_number = 0, max_enemies = 3, boss=False):
        #Map specifications
        self.max_steps = max_steps
        self.safe_zones = []
        self.safe_zones_number = safe_zones_number
        self.max_enemies = max_enemies
        self.boss = boss
        self.current_encounter = None
        
        #Team
        self.team = team

        #Rewards and difficulty
        self.succes_flag = False
        self.team_level = self.team.get_team_level()
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
            if self.team:
                self.current_encounter = self.rooms_dict[key](self.team, max_enemies=self.max_enemies, room_number=key, team_level=self.team_level) 
                self.current_encounter.begin_encounter()
                self.generate_rewards()
            else:
                return None
        self.succes_flag = True
    
    def generate_rewards(self):
        if not self.team:
            return None
        current_rewards = {}
        #Gold
        base_gold = 150
        earned_gold = int(base_gold * (self.team_level ** 1.2) * random.uniform(0.8, 1.2))
        self.rewards["gold"] += earned_gold
        current_rewards["gold"] = earned_gold
        #Item
        ticket = random.random()
        if ticket > 0.5:
            item = self.item_generator.generate_item(difficulty_key=self.difficulty_key, level=self.team_level) 
            self.rewards["items"].append(item)
            current_rewards["items"] = [item]
        #Exp
        base_exp = 50
        earned_exp = int(base_exp * self.current_encounter.n_enemies * (self.team_level ** 1.2)) #we use team_level because monster levels are based on team level
        self.rewards["exp"] += earned_exp
        current_rewards["exp"] = earned_exp

        self.check_rewards(current_rewards, message="Your rewards after completing room:\n")
        
    def grant_rewards(self):
        self.team.stash.wallet.earn(self.rewards["gold"])
        for item in self.rewards["items"]:
            self.team.stash.add_item(item)
        for player in self.team.get_team_members():
            player.gain_exp(self.rewards["exp"])
    
    def check_rewards(self, rewards=None, message="Your all rewards after the adventure:\n"):
        if not rewards:
            rewards = self.rewards
        gold = str(rewards["gold"])
        items_lst = [item.get_name() for item in rewards.get("items", [])]
        item_lst = ", ".join(items_lst)
        exp = str(rewards["exp"])
        rewards_str = f"Items: {item_lst}\nGold: {gold}\nExp: {exp}"
        show_message(message + rewards_str)
        
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__