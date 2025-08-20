from Game.Encounter.Encounter import HostileEncounter, SafeEncounter

class Map:
    def __init__(self, max_steps=4, safe_zones=[3, 6, 9], players=None): #TODO max_steps increase
        self.max_steps = max_steps
        self.current_position = 0
        self.safe_zones = safe_zones
        self.players = players
        self.current_encounter = None
        self.encounter_type = None 

    def generate_encounter(self):
        if self.current_position not in self.safe_zones:
            self.current_encounter = HostileEncounter(self.players, max_enemies=3) #TODO adjusting to many encounters
        else:
            self.current_encounter = SafeEncounter(self.players)
    
    def __eq__(self, other):
        return isinstance(other, Map) and self.__dict__ == other.__dict__
    
    def take_step(self):
        self.current_position += 1