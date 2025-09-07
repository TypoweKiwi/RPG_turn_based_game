from PlayerClasses.Classes import classes
from PlayerClasses.Team import Team
from Game.AdventureHub.AdventureHub import AdventureHub
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
            {"name": "Continue game - Unlocked after starting/loading game", "value": lambda: None},
            {"name": "Save game - Unlocked after starting/loading game", "value":  lambda: None},
            {"name": "Check rules", "value": self.show_rules},
            {"name": "Exit game", "value": self.end_game}
        ]
    
    def change_menu_options(self, continue_name, continue_value, save_name, save_value):
        self.menu_choices[2]["name"] = continue_name
        self.menu_choices[2]["value"] = continue_value
        
        self.menu_choices[3]["name"] = save_name
        self.menu_choices[3]["value"] = save_value


    def unlock_menu_options(self):
        self.change_menu_options(
            continue_name="Continue game",
            continue_value=self.continue_game,
            save_name="Save game",
            save_value=self.save_game_state
            )
    
    def lock_menu_options(self):
        self.change_menu_options(
            continue_name="Continue game - Unlocked after starting",
            continue_value=lambda: None,
            save_name="Save game - Unlocked after starting",
            save_value=lambda: None
            )
    
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
    
    def save_game_state(self): 
        save_name = "Team." + self.players.name + "." + datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + ".txt"
        save_game(save_name, self.players, self.map) 
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
    
    def start_menu(self): 
        choice = make_query(message="\nWelcome! \nChoose action: ", choices=self.menu_choices)
        choice()

    def continue_game(self):
        self.state = Game_state.running
    
    def enter_adventure_hub(self):
        self.adventure_hub.make_decision()
        if self.adventure_hub.exit_flag:
            self.state = Game_state.idle
            if not self.adventure_hub.players:
                self.lock_menu_options()
        