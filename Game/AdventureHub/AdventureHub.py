import math
from Game.UI.HubUI import HubUI, make_query
from Game.Map import Map
from Game.Shop import Shop
from Game.Temple import Temple
from Game.Tavern import Tavern

class AdventureHub:
    def __init__(self, team):
        self.team = team
        self.n_completed_adventures = 0
        self.exit_flag = False
        self.shop = Shop(self.team)
        self.hub_ui = HubUI(self.team, self.shop)
        self.temple = Temple(self.team)
        self.tavern = Tavern(self.team)
    
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
    
    def update_hub(self):
        self.shop.refresh_shop()
        self.temple.update_cost()
        self.tavern.refresh_adventurer_list()

    def start_adventure(self):
        map = self.choose_adventure()
        if not map:
            return None
        map.begin_adventure()
        if map.succes_flag:
            map.grant_rewards()
            self.update_hub()
        else:
            self.exit_hub()
    
    def decision_loop(self,  choices): #One of the choices need to have value None!
        while True:
            choice = make_query(choices=choices)
            if not choice:
                break
            choice()

    def open_shop(self):
        choices = [
            {"name": "Check stock", "value": self.hub_ui.check_stock},
            {"name": "Buy item", "value": self.hub_ui.buy_item},
            {"name": f"Refresh shop - cost: {self.shop.refresh_price}", "value": self.shop.buy_refresh_shop},
            {"name": f"Current team gold: {self.team.stash.wallet.gold_value}", "value": lambda: None},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(choices=choices)

    def open_stash(self):
        choices = [
            {"name": "View items in stash", "value": self.hub_ui.view_items},
            {"name": "Sort/fitr viewed items", "value": self.team.stash.sort_stash},
            {"name": "Change player inventory", "value": self.hub_ui.modify_player_inventory},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(choices=choices)

    def check_team_info(self):
        choices = [
            {"name": "Check team stats", "value": self.hub_ui.show_vital_stats},
            {"name": "Check team resistances", "value": self.hub_ui.show_resistances},
            {"name": "Check team skills", "value": lambda: self.hub_ui.show_skills(self.team.choose_player())},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(choices=choices)

    def visit_temple(self):
        choices = [
            {"name": "Heal team", "value": self.temple.heal_team},
            {"name": "Recover team mana", "value": self.temple.recover_team_mana},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(choices=choices)

    def visit_tavern(self):
        choices = [
            {"name": "Recruit adventurer", "value": self.tavern.recruit_adventurer},
            {"name": "Retire the adventurer", "value": self.tavern.retire_adventurer},
            {"name": "Back", "value": None}
        ]
        self.decision_loop(choices=choices)

    def exit_hub(self):
        self.exit_flag = True

    def get_hub_options(self):
        choices = [
            {"name": "Start expedition", "value": self.start_adventure},
            {"name": "Visit shop", "value": self.open_shop},
            {"name": "Open stash/inventory", "value": self.open_stash},
            {"name": "Team recovery", "value": self.visit_temple},
            {"name": "Check team information", "value": self.check_team_info},
            {"name": "Visit tavern", "value": self.visit_tavern},
            {"name": "Exit to menu", "value": self.exit_hub}
        ]
        return choices
    
    def __eq__(self, other):
        return isinstance(other, AdventureHub) and self.__dict__ == other.__dict__

    def to_save_dict(self):
        return {
            "team": self.team.to_save_dict(),
            "n_completed_adventures": self.n_completed_adventures,
            "shop": self.shop.to_save_dict(),
            "tavern": self.tavern.to_save_dict(),
            "temple": self.temple.to_save_dict()
        }
    
    def load_save_dict(self, save_dict):
        self.team.load_save_dict(save_dict["team"])
        self.n_completed_adventures = save_dict["n_completed_adventures"]
        self.shop.load_save_dict(save_dict["shop"])
        self.tavern.load_save_dict(save_dict["tavern"])
        self.temple.load_save_dict(save_dict["temple"])

        
        