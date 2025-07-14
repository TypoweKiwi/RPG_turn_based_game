from DamageCalculations.Reducing_damage import reduce_dmg
from DamageCalculations.Type import DamageType
import random

class Player: #TODO move speed stat -> basic stats dict -> key "move_speed"
    def __init__(self, name, basic_stat_dict, hostile = False):
        self.name = name
        self.max_hp = basic_stat_dict["max_hp"]
        self.health_points = basic_stat_dict["max_hp"]
        self.max_mp = basic_stat_dict["max_mp"]
        self.mana_points = basic_stat_dict["max_mp"]
        self.attack_damage = basic_stat_dict["attack_damage"]
        self.critical_chance = basic_stat_dict["crit_chance"]
        self.ability_power = basic_stat_dict["ability_power"]
        self.speed = basic_stat_dict["speed"]
        self.resistance = basic_stat_dict["resistance"]
        self.skills = []
        self.hostile = hostile

    def take_hit(self, damage, type):
        self.health_points -= reduce_dmg(damage, self.resistance[type])

    def get_damage_multiplayers(self):
        dict = {
            "AD": self.attack_damage,
            "AP": self.ability_power,
            "Crit": self.critical_chance
        }
        return dict
    
    def check_skills(self):
        avalible_skills = []
        for skill in self.skills:
            if skill.cost < self.mana_points:
                avalible_skills.append({
                    "name": str(skill),
                    "description": skill.desc,
                    "value": skill,
                })
            else:
                avalible_skills.append({
                    "name": str(skill) + "(Not enough MP)",
                    "description": skill.desc,
                    "value": None
                })
        return avalible_skills

    def __str__(self):
        return f"{self.name} Hp: {self.health_points}/{self.max_hp}"
