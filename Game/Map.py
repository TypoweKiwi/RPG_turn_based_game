from Monster.Monsters import monsters
import random
from enum import Enum

class Encounter_type(Enum):
    fight = 1
    rest = 2

class Map:
    def __init__(self, max_steps=10, safe_zone=[3, 6, 9], max_enemies=3):
        self.max_steps = max_steps
        self.current_position = 1
        self.safe_zone = safe_zone
        self.max_enemies = max_enemies
        self.current_encounter = []
        self.encounter_type = None 

    def generate_encounter(self):
        self.current_encounter.clear()
        if self.current_position not in self.safe_zone:
            self.encounter_type = Encounter_type.fight
            n_enemies = random.randint(1, self.max_enemies)
            for i in range(n_enemies):
                monster_key = random.choice(monsters)
                self.current_encounter.append(monsters[monster_key]())
        else:
             self.encounter_type = Encounter_type.rest
    
    def take_step(self):
        self.current_position += 1