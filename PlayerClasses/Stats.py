class Stats:
    def __init__(self, basic_stat_dict):
        self.max_hp = basic_stat_dict["max_hp"]
        self.max_mp = basic_stat_dict["max_mp"]
        self.max_stamina = basic_stat_dict["max_stamina"]
        self.attack_damage = basic_stat_dict["attack_damage"]
        self.critical_chance = basic_stat_dict["critical_chance"]
        self.ability_power = basic_stat_dict["ability_power"]
        self.speed = basic_stat_dict["speed"]
        self.resistance = basic_stat_dict["resistance"]

        self.health_points = 0
        self.mana_points = 0
        self.stamina = 0
    
    def __add__(self, other):
        return Stats({
            "max_hp": self.max_hp + other.max_hp,
            "max_mp": self.max_mp + other.max_mp,
            "attack_damage": self.attack_damage + other.attack_damage,
            "critical_chance": self.critical_chance + other.critical_chance,
            "ability_power": self.ability_power + other.ability_power,
            "speed": self.speed + other.speed,
            "resistance": {key: self.resistance[key] + other.resistance[key] for key in self.resistance}
        })