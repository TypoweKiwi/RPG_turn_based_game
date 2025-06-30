from Monster.Monsters import monsters
import random

class Map:
    def __init__(self, steps=10, safe_zone=[3, 6, 9], max_enemies=3):
        self.steps = steps
        self.current_position = 1
        self.safe_zone = safe_zone
        self.max_enemies = max_enemies

    def generate_encounter(self):
        if self.current_position is not self.safe_zone:
            n_enemies = random.randint(1, self.max_enemies)
            
            
        else:
            #safe zone 
            #TODO