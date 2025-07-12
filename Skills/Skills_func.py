from DamageCalculations.Type import DamageType
import random

def basic_attack_func(stats_dict, target):
    attack_damage = stats_dict["AD"]
    crit_chance = stats_dict["Crit"]
    ticket = random.random()
    damage = attack_damage*2 if crit_chance >= ticket else attack_damage
    target.take_hit(damage, DamageType.physical)

def holy_smite_func(stats_dict, target):
    skill_damage = 5
    ability_power = stats_dict["AP"]
    damage = skill_damage*ability_power
    target.take_hit(damage, DamageType.holy)

def heal_func(stats_dict, target):
    heal_amount = 10
    target.health_points = min(target.max_hp, target.health_points + heal_amount)

def prayer_func(stats_dict, targets):
    skill_damage = 3
    ability_power = stats_dict["AP"]
    damage = skill_damage*ability_power
    for target in targets:
        target.take_hit(damage, DamageType.holy)
          
    