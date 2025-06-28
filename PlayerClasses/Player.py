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

    def basic_attack(self, target):
        ticket = random.random(0.01, 1)
        damage = self.attack_damage *2 if self.critical_chance >= ticket else self.attack_damage
        target.take_hit(damage, DamageType.physical)
    
    def take_hit(self, damage, type):
        self.health_points -= reduce_dmg(damage, self.resistance[type])
    
    def __str__(self):
        return f"Player {self.name} Hp: {self.health_points}/{self.max_hp}"
    
    def ability_1(self):
        pass

    def ability_2(self):
        pass

    def ability_3(self):
        pass

    def get_abilities(self):
        pass