from DamageCalculations.Reducing_damage import reduce_dmg

class Player:
    def __init__(self, name, basic_stat_dict):
        self.name = name
        self.max_hp = basic_stat_dict["max_hp"]
        self.health_points = basic_stat_dict["max_hp"]
        self.attack_damage = basic_stat_dict["attack_damage"]
        self.ability_power = basic_stat_dict["ability_power"]
        self.resistance = basic_stat_dict["resistance"]

    def hit(self, target, damage, type):
        target.take_hit(damage, type)
    
    def take_hit(self, damage, type):
        self.health_points -= reduce_dmg(damage, self.res_dict[type])
    
    def __str__(self):
        return f"Player {self.name} Hp: {self.health_points}/{self.max_hp}"