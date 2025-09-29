from Game.UI.Choices_func import show_message, make_query
from PlayerClasses.Classes import classes
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