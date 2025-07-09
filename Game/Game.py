from PlayerClasses.Classes import classes
from Game.Map import Map
from InquirerPy import inquirer
from enum import Enum

class Game_state(Enum):
    idle = 1
    running = 2
    encounter = 3
    end = 4

def make_query(message, choices):
    choice = inquirer.select(
            message=message,
            choices= choices,
        ).execute()
    return choice 

class Game:
    def __init__(self):
        self.player = None
        self.map = None 
        self.state = Game_state.idle

    def create_new_game(self):
        choice = make_query("Chose your class:", [element for element in classes])
        print(f"Your class choice: {choice}")

        name = input("Write your name")
        self.player = classes[choice](name)
        self.map = Map()
        self.state = Game_state.running
    
    def move_a_step(self):
        self.map.take_step
        self.map.generate_encounter()
        self.map.current_encounter.begin_encounter(self.player)
        

    def check_end(self):
        choice = make_query("Do you wish to play again?", ["yes", "No"])
        if choice == "No":
            self.state = Game_state.end