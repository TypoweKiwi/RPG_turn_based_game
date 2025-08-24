from PlayerClasses.Classes import classes
from PlayerClasses.Team import Team
from Game.AdventureHub import AdventureHub
from enum import Enum
from Game.UI.Choices_func import make_query, show_message
from Game.Saves.Saves_game_func import save_game, return_save_name, save_path
from Game.Saves.Load_game_func import load_game
import datetime
import os 


class Game_state(Enum):
    idle = 1
    running = 3
    encounter = 4
    end = 5

class Game:
    def __init__(self):
        self.players = None #TODO check if there is point in keeping players in game class
        self.adventure_hub = None 
        self.state = Game_state.idle

        self.menu_choices = [
            {"name": "Start new game", "value": self.create_new_game},
            {"name": "Load game", "value": self.load_game_state},
            {"name": "Continue game", "value": self.continue_game, "disabled": "Available after starting the game"},
            {"name": "Save game", "value": "save", self.save_game_state: "Available after starting the game"},
            {"name": "Check rules", "value": self.show_rules},
            {"name": "Exit game", "value": self.end_game}
        ]
    
    def unlock_menu_options(self):
        for choice in self.menu_choices:
            if choice["name"] in ("Continue game", "Save game"):
                choice.pop("disabled", None)

    def create_new_game(self): 
        team_name = input("Write your team name: ")
        n_team = make_query("Chose your team size: ", [1, 2, 3, 4])
        self.players = Team(name=team_name)
        for i in range(n_team):
            choice = make_query(f"Chose your {i+1} team member:", [element for element in classes])
            print(f"Your choice: {choice}")
            self.players.add_player(classes[choice]())
        
        self.adventure_hub = AdventureHub(players=self.players)
        self.state = Game_state.running
        self.unlock_menu_options()
    
    def save_game_state(self): #TODO eleminate recursion if stack issues occur 
        save_name = "Team." + self.players.name + "." + datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + ".txt"
        save_game(save_name, self.players, self.map) #TODO save_path name collision 
        show_message("Game saved successfully.")
        self.step_menu()

    def load_game_state(self):
        saves_lst = [{"name": return_save_name(save), "value": save} for save in os.listdir(save_path) if save.endswith(".txt")]
        saves_lst.append({"name": "Back", "value": None})
        choice = make_query(message="Which save you wish to load?", choices=saves_lst)
        if choice is None:
            self.start_menu()
        else: 
            self.map = load_game(save_name=choice)
            self.players = map.players
            show_message("Game loaded successfully.")
            self.state = Game_state.running
            self.unlock_menu_options()
    
    def show_rules(self):
        show_message("Rules not implemented yet")
    
    def end_game(self):
        self.state = Game_state.end
    
    def start_menu(self): #TODO moving menu methods to additional game menu class
        choice = make_query(message="\nWelcome! \nChoose action: ", choices=self.menu_choices)
        choice()

    def continue_game(self):
        self.state = Game_state.running
    
    def enter_adventure_hub(self):
        self.adventure_hub.make_decision()
        