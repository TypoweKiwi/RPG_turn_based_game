from Game.Encounter.Encounter import HostileEncounter, SafeEncounter
import random

class Map:
    def __init__(self, players, max_steps=3, safe_zones_number = 0, max_enemies = 3, boss=False):
        self.max_steps = max_steps
        self.current_position = 0
        self.players = players
        self.safe_zones = []
        self.safe_zones_number = safe_zones_number
        self.max_enemies = max_enemies
        self.boss = boss
        self.current_encounter = None
        self.succes_flag = False
        self.rewards = []

    def generate_safezones(self):
        self.safe_zones = random.sample(range(1, self.max_steps+1), self.safe_zones_number)

    def generate_encounter(self, step):
        if step not in self.safe_zones:
            self.current_encounter = HostileEncounter(self.players, max_enemies=3, room_number=step) #TODO adjusting to many encounters
        else:
            self.current_encounter = SafeEncounter(self.players, room_number=step)
    
    def begin_adventure(self):
        self.generate_safezones()
        for step in range(self.max_steps):
            if self.players:
                self.generate_encounter(step+1)
                self.current_encounter.begin_encounter()
            else:
                return None
        self.succes_flag = True
    
    def grant_rewards(self): #TODO adding to stash finded items and gold
        pass
    
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__