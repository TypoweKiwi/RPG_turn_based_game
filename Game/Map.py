import random
from enum import Enum
from Game.Encounter import Hostile_encounter

class Encounter_type(Enum):
    fight = 1
    rest = 2

class Map:
    def __init__(self, max_steps=1, safe_zone=[3, 6, 9]): #TODO max_steps increase
        self.max_steps = max_steps
        self.current_position = 1
        self.safe_zone = safe_zone
        self.current_encounter = None
        self.encounter_type = None 

    def generate_encounter(self):
        if self.current_position not in self.safe_zone:
            self.encounter_type = Encounter_type.fight
            self.current_encounter = Hostile_encounter("descriedpsa", 1) #TODO adjusting to many encounters
        else:
             self.encounter_type = Encounter_type.rest #TODO self.current encounter safe
    
    def take_step(self):
        self.current_position += 1