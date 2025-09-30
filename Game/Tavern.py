from Game.UI.Choices_func import show_message, make_query
from PlayerClasses.Classes import classes
from PlayerClasses.Player import Player
import random

class Tavern():
    def __init__(self, team, max_team_size=4):
        self.team = team
        self.max_team_size = max_team_size
        self.table_size = 3
        self.calculate_adventurer_cost()
        self.refresh_adventurer_list()

    def calculate_adventurer_cost(self):
        self.cost = int(1000*(self.team.get_team_level()**1.1))
    
    def refresh_adventurer_list(self):
        self.adventurers_list = []
        for i in range(self.table_size):
            self.adventurers_list.append(classes[random.choice(list(classes.keys()))](level=max(self.team.get_team_level()-2, 1))) 
    
    def choose_adventurer(self):
        message = f"Choose adventurer to recruit (cost: {self.cost}): "
        choices = [{"name": adventurer.get_name() + f" (level {adventurer.get_level()})", "value": adventurer} for adventurer in self.adventurers_list]
        choices.append({"name": "Back", "value": None})
        choice = make_query(message=message, choices=choices)
        if choice:
            if self.team.stash.wallet.try_payment(self.cost):
                self.team.add_player(choice)
                self.adventurers_list.remove(choice)
        
    def recruit_adventurer(self):
        if len(self.team) >= self.max_team_size:
            show_message("Your team is already full. You cannot recruit more adventurers.")
            return None
        else:
            self.calculate_adventurer_cost()
            self.choose_adventurer()

    def retire_adventurer(self):
        if len(self.team) == 1:
            show_message("You cannot retire the last member of your team.")
            return None
        show_message("If you retire team member, you will lose all their items.")
        player = self.team.choose_player()
        choice = make_query(message=f"Are you sure you want to retire {player.get_name()}?", choices=["Yes", "No"])
        if choice == "Yes":
            self.team.remove_player(player)
    
    def __eq__(self, other):
        if not isinstance(other, Tavern):
            return False
        
        differences = []
        for key in self.__dict__:
            self_val = self.__dict__[key]
            other_val = getattr(other, key, None)
            if self_val != other_val:
                differences.append((key, self_val, other_val))
        
        if differences:
            print("Tavern are not equal. Differences:")
            for key, self_val, other_val in differences:
                print(f"Field '{key}': self={self_val} | other={other_val}")
            return False
        
        return True
    
    def to_save_dict(self):
        save_dict = {}
        save_dict["cost"] = self.cost
        save_dict["adventurers_list"] = [adventurer.to_save_dict() for adventurer in self.adventurers_list]
        return save_dict
    
    def load_save_dict(self, save_dict):
        self.cost = save_dict["cost"]
        self.adventurers_list = []
        for adventurer_save_dict in save_dict["adventurers_list"]:
            adventurer = Player(name="", basic_stat_dict={})
            adventurer.load_save_dict(adventurer_save_dict)
            self.adventurers_list.append(adventurer)
        