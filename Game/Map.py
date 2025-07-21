import random
from enum import Enum
from Game.Encounter.Encounter import HostileEncounter, SafeEncounter

class Map:
    def __init__(self, max_steps=1, safe_zone=[3, 6, 9], players=None): #TODO max_steps increase
        self.max_steps = max_steps
        self.current_position = 1
        self.safe_zone = safe_zone
        self.players = players
        self.current_encounter = None
        self.encounter_type = None 

    def generate_encounter(self):
        if self.current_position not in self.safe_zone:
            self.current_encounter = HostileEncounter(self.players, 1) #TODO adjusting to many encounters
        else:
            self.current_encounter = SafeEncounter(self.players)
    
    def take_step(self):
        self.current_position += 1