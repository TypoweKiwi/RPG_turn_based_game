from PlayerClasses.Classes import classes
from PlayerClasses.Team import Team
from Game.Map import Map
from enum import Enum
from Game.Choices_func import make_query, show_message

class Game_state(Enum):
    idle = 1
    running = 2
    encounter = 3
    end = 4

class Game:
    def __init__(self):
        self.players = None
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
    
    def save_game_state(self):
        pass

    def load_game_state(self):
        pass
    
    def move_a_step(self):  #TODO some option after compliting encounter to rest
        self.map.take_step()
    
    def begin_current_encounter(self):
        self.map.generate_encounter()
        self.map.current_encounter.begin_encounter()
    
    def check_state(self):
        if self.map.current_position == self.map.max_steps:
            self.state = Game_state.idle

    def check_if_win(self):
        if self.map.players.get_team_members:
            show_message("\nYour team completes the adventure. You won!")
        else:
            show_message("\nYour team did not survived. You lost.")

    def check_end(self):
        choice = make_query("Do you wish to play again?", ["yes", "No"])
        if choice == "No":
            self.state = Game_state.end