from DamageCalculations.Reducing_damage import reduce_dmg
from DamageCalculations.Type import DamageType
import random

class Player:
    def __init__(self, name, basic_stat_dict):
        self.name = name
        self.max_hp = basic_stat_dict["max_hp"]
        self.health_points = basic_stat_dict["max_hp"]
        self.max_mp = basic_stat_dict["max_mp"]
        self.mana_points = basic_stat_dict["max_mp"]
        self.attack_damage = basic_stat_dict["attack_damage"]
        self.critical_chance = basic_stat_dict["crit_chance"]
        self.ability_power = basic_stat_dict["ability_power"]
        self.resistance = basic_stat_dict["resistance"]
        self.skills = []

    def take_hit(self, damage, type):
        self.health_points -= reduce_dmg(damage, self.resistance[type])

    def get_damage_multiplayers(self):
        dict = {
            "AD": self.attack_damage,
            "AP": self.ability_power,
            "Crit": self.critical_chance
        }
        return dict
    
    def __str__(self):
        return f"{self.name} Hp: {self.health_points}/{self.max_hp}"
