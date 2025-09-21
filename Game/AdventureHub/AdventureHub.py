import math
from Game.UI.HubUI import HubUI, make_query, show_message
from Game.Map import Map
from Game.Shop import Shop

class AdventureHub:
    def __init__(self, players):
        self.team = players
        self.n_completed_adventures = 0
        self.exit_flag = False
        self.shop = Shop(self.team)
        self.hub_ui = HubUI(self.team, self.shop)
    
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
            presets[key]["cost"] = i*int(base_cost * (1 + self.team.get_team_level() ** 1.1))
        return presets

    def choose_adventure(self): #TODO Refactorize coode -> split function logic
        presets = self.generate_map_preset()
        preset = self.hub_ui.choose_map(presets)
        if not preset:
            return None
        return Map(
            team=self.team, 
            max_steps=preset["max_steps"],
            safe_zones_number=preset["safe_zones_number"],
            max_enemies=preset["max_enemies"],
            boss = preset["boss"],
            difficulty_key= preset["difficulty_key"]
        )
    
    def start_adventure(self):
        map = self.choose_adventure()
        if not map:
            return None
        map.begin_adventure()
        if map.succes_flag:
            map.grant_rewards()
            self.shop.refresh_shop()
        else:
            self.exit_hub()
    
    def decision_loop(self, message, choices): #One of the choices need to have value None!
        while True:
            choice = make_query(message, choices)
            if not choice:
                break
            choice()

    def open_shop(self):
        message = "Choose action"
        choices = [
            {"name": "Check stock", "value": self.hub_ui.check_stock},
            {"name": "Buy item", "value": self.hub_ui.buy_item},
            {"name": f"Refresh shop - cost: {self.shop.refresh_price}", "value": self.shop.buy_refresh_shop},
            {"name": f"Current team gold: {self.team.stash.wallet.gold_value}", "value": lambda: None},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(message, choices)

    def open_stash(self):
        message = "Choose action"
        choices = [
            {"name": "View items in stash", "value": self.hub_ui.view_items},
            {"name": "Sort/fitr viewed items", "value": self.team.stash.sort_stash},
            {"name": "Change player inventory", "value": self.hub_ui.modify_player_inventory},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(message, choices)

    def check_team_info(self):
        message = "Choose action"
        choices = [
            {"name": "Check team stats", "value": self.hub_ui.show_vital_stats},
            {"name": "Check team resistances", "value": self.hub_ui.show_resistances},
            {"name": "Check team skills", "value": lambda: self.hub_ui.show_skills(self.team.choose_player())},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(message, choices)

    def team_recovery(self):
        pass

    def recruit_adventurer(self):
        pass

    def exit_hub(self):
        self.exit_flag = True

    def get_hub_options(self):
        choices = [
            {"name": "Start expedition", "value": self.start_adventure},
            {"name": "Visit shop", "value": self.open_shop},
            {"name": "Open stash/inventory", "value": self.open_stash},
            {"name": "Team recovery", "value": self.team_recovery},
            {"name": "Check team information", "value": self.check_team_info},
            {"name": "Recruit adventurer", "value": self.recruit_adventurer},
            {"name": "Exit to menu", "value": self.exit_hub}
        ]
        return choices