from PlayerClasses.Classes import classes
from Game.Map import Map
from InquirerPy import inquirer
from enum import Enum

class Games_state(Enum):
    idle = 1
    running = 2
    end = 3

class Game:
    def __init__(self):
        self.player = None
        self.map = None 
        self.state = Game_state.idle

    def create_new_game(self):
        choice = inquirer.select(
            message="Chose your class:",
            choices= [element for element in classes],
        ).execute()
        print(f"Your class choice: {choice}")

        name = input("Write your name")
        self.player = classes[choice](name)
        self.map = Map()
        self.state = Game_state.running