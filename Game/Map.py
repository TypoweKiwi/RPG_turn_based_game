from Game.Encounter.Encounter import HostileEncounter, SafeEncounter
import random

class Map:
    def __init__(self, players, max_steps=3, safe_zones_number = 0, max_enemies = 3):
        self.max_steps = max_steps
        self.current_position = 0
        self.players = players
        self.safe_zones = []
        self.safe_zones_number = safe_zones_number
        self.max_enemies = max_enemies
        self.current_encounter = None
        self.succes_flag = False

    def generate_safezones(self):
        self.safe_zones = random.sample(range(1, self.max_steps+1), self.safe_zones_number)

    def generate_encounter(self, step):
        if step not in self.safe_zones:
            self.current_encounter = HostileEncounter(self.players, max_enemies=3) #TODO adjusting to many encounters
        else:
            self.current_encounter = SafeEncounter(self.players)
    
    def begin_adventure(self):
        self.generate_safezones()
        for step in range(self.max_steps):
            if self.players:
                self.generate_encounter(step+1)
                self.current_encounter.begin_encounter()
            else:
                return None
        self.succes_flag = True
    
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__