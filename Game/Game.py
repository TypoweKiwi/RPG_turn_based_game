from PlayerClasses.Classes import classes
from Game.Map import Map
from enum import Enum
from Game.Choices_func import make_query

class Game_state(Enum):
    idle = 1
    running = 2
    encounter = 3
    end = 4

class Game:
    def __init__(self):
        self.player = None
        self.map = None 
        self.state = Game_state.idle

    def create_new_game(self):
        choice = make_query("Chose your class:", [element for element in classes])
        print(f"Your class choice: {choice}")

        self.player = classes[choice]()
        self.map = Map()
        self.state = Game_state.running
    
    def move_a_step(self): #TODO Chyba coś tutaj trzeba zrobić tak przeczuwam 
        self.map.take_step
        self.map.generate_encounter()
        self.map.current_encounter.begin_encounter(self.player)

    def check_end(self):
        choice = make_query("Do you wish to play again?", ["yes", "No"])
        if choice == "No":
            self.state = Game_state.end