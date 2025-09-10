import math
from Game.UI.HubUI import HubUI, make_query, show_message
from Game.Map import Map

class AdventureHub:
    def __init__(self, players, difficulty_factor=1):
        self.players = players
        self.difficulty_factor = difficulty_factor #Implement difficulty_factor to options in games class let player choose difficulty of game :)
        self.n_completed_adventures = 0
        self.exit_flag = False
        self.hub_ui = HubUI()
    
    def make_decision(self):
        self.exit_flag = False 
        choices = self.get_hub_options()
        choice = make_query(message="Choose hub action", choices=choices)
        choice()
    
    def generate_map_preset(self):
        if (self.n_completed_adventures+1)%10 == 0: #Every 10th room has boss and player is forced to face him
            presets = {"boss":{"boss":True}}
        else:
            presets = {
                "short":{"boss":False, "difficulty_key": "short"},
                "medium":{"boss":False, "difficulty_key": "medium"},
                "long":{"boss":False, "difficulty_key": "long"}
            }
        base_steps = min(6, 3 + math.floor(self.n_completed_adventures/10))
        max_enemies = base_steps = min(5, 3 + math.floor(self.n_completed_adventures/10))
        base_cost = 500
        for i, key in enumerate(presets):
            presets[key]["max_steps"] = base_steps + i*3
            presets[key]["safe_zones_number"] = i
            presets[key]["max_enemies"] = max_enemies
            presets[key]["cost"] = i*int(base_cost * (1 + self.players.get_team_level() ** 1.1))
        return presets

    def choose_adventure(self):
        presets = self.generate_map_preset()
        preset = self.hub_ui.choose_map(presets)
        while preset["cost"] > self.players.stash.wallet: #TODO payment class system
            show_message(f"You do not have enough gold to buy this map. \nCurrent gold: {self.players.stash.wallet} \nMap cost: {preset['cost']}")
            preset = self.hub_ui.choose_map(presets)
        self.players.stash.wallet -= preset["cost"]
        return Map(
            players=self.players, 
            max_steps=preset["max_steps"],
            safe_zones_number=preset["safe_zones_number"],
            max_enemies=preset["max_enemies"],
            boss = preset["boss"],
            difficulty_key= preset["difficulty_key"]
        )
    
    def start_adventure(self): #TODO check what happend if player dies during expedition
        map = self.choose_adventure()
        map.begin_adventure()
        if map.succes_flag:
            map.grant_rewards()
        else:
            self.exit_hub()

    def visit_wizard(self):
        pass

    def open_shop(self):
        pass

    def open_stash(self):
        pass

    def check_team_info(self):
        pass

    def team_recovery(self):
        pass

    def recruit_adventurer(self):
        pass

    def exit_hub(self):
        self.exit_flag = True

    def get_hub_options(self):
        choices = [
            {"name": "Start expedition", "value": self.start_adventure},
            {"name": "Visit wizard", "value": self.visit_wizard},
            {"name": "Visit shop", "value": self.open_shop},
            {"name": "Open stash", "value": self.open_stash},
            {"name": "Team recovery", "value": self.team_recovery},
            {"name": "Check team information", "value": self.check_team_info},
            {"name": "Recruit adventurer", "value": self.recruit_adventurer},
            {"name": "Exit to menu", "value": self.exit_hub}
        ]
        return choices