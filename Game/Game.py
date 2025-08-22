from PlayerClasses.Classes import classes
from PlayerClasses.Team import Team
from Game.Map import Map
from enum import Enum
from Game.Choices_func import make_query, show_message
from Game.Saves.Saves_game_func import save_game, return_save_name, save_path
from Game.Saves.Load_game_func import load_game
import datetime
import os 


class Game_state(Enum):
    idle = 1
    running = 2
    encounter = 3
    end = 4

class Game:
    def __init__(self):
        self.players = None #TODO check if there is point in keeping players in game class
        self.map = None 
        self.state = Game_state.idle

    def create_new_game(self): 
        n_team = make_query("Chose your team size: ", [1, 2, 3, 4])
        team_name = input("Write your team name: ")
        self.players = Team(name=team_name)
        for i in range(n_team):
            choice = make_query(f"Chose your {i+1} team member:", [element for element in classes])
            print(f"Your choice: {choice}")
            self.players.add_player(classes[choice]())
        
        self.map = Map(players=self.players)
        self.state = Game_state.running
    
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
    
    def start_menu(self): #TODO moving menu methods to additional game menu class
        choices = [
            {"name": "Start new game", "value": self.create_new_game},
            {"name": "Load game", "value": self.load_game_state},
            {"name": "Check rules", "value": None},
            {"name": "Options", "value": None}
        ]

        choice = make_query(message="\nWelcome! \nChoose action: ", choices=choices)
        if choice is None: #TODO after implementing check rules and options remove this condition
            show_message("This option is still in progres")
            self.start_menu()
        else:
            choice()

    def step_menu(self):  
        choices = [
            {"name": "Take step", "value": lambda: None},
            {"name": "Save game", "value": self.save_game_state},
            {"name": "Rest", "value": lambda: None}  #TODO Rest option
        ]
        make_query(message="\nChoose next action: ", choices=choices)()

    def begin_current_encounter(self):
        self.map.generate_encounter()
        self.map.current_encounter.begin_encounter()

    def take_step(self):
        self.map.take_step()
        self.begin_current_encounter()
        self.check_state()
        if self.state == Game_state.running:
            self.step_menu()

    def check_state(self):
        if self.map.current_position == self.map.max_steps or self.players.get_team_members() == []:
            self.state = Game_state.idle

    def check_if_win(self):
        if self.map.players.get_team_members():
            show_message("\nYour team completes the adventure. You won!")
        else:
            show_message("\nYour team did not survived. You lost.")

    def check_end(self):
        choice = make_query("Do you wish to play again?", ["yes", "No"])
        if choice == "No":
            self.state = Game_state.end