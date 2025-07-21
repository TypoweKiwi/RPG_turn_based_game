from DamageCalculations.Type import DamageType
import random
#TODO BALANCE - Basic stats dict - skill damage - skill resistacne

def apply_damage(skill_damage, modifier, target, damage_type, criticality=False, crit_chance=0):
    damage = skill_damage*modifier
    if criticality:
        ticket = random.random() 
        damage = damage*2 if crit_chance >= ticket else damage
    target.take_hit(damage, damage_type)

def basic_attack_func(stats_dict, target):
    attack_damage = stats_dict["AD"]
    apply_damage(skill_damage=attack_damage, modifier=1, target=target, damage_type=DamageType.physical, criticality=True, crit_chance=stats_dict["crit"])

def holy_smite_func(stats_dict, target):
    skill_damage = 5
    apply_damage(skill_damage=skill_damage, modifier=stats_dict["AP"], target=target, damage_type=DamageType.holy)

def heal_func(stats_dict, target):
    ability_power = stats_dict["AP"]
    skill_power = 3
    heal_amount = skill_power*int(ability_power*0.5)
    target.health_points = min(target.max_hp, target.health_points + heal_amount)
    print(f"{target.name} was healed {heal_amount} HP")

def prayer_func(stats_dict, targets):
    skill_damage = 3
    for target in targets:
        apply_damage(skill_damage=skill_damage, modifier=stats_dict["AP"], target=target, damage_type=DamageType.holy)

def barbaric_charge_func(stats_dict, targets):
    skill_damage = 3
    for target in targets:
        apply_damage(skill_damage=skill_damage, modifier=stats_dict["AD"], target=target, damage_type=DamageType.physical)

def heavy_strike_func(stats_dict, target):
    skill_damage = 5
    apply_damage(skill_damage=skill_damage, modifier=stats_dict["AD"], target=target, damage_type=DamageType.physical, criticality=True, crit_chance=stats_dict["crit"])

def battle_cry_func(stats_dict, targets):
    skill_damage = 4
    for target in targets:
        apply_damage(skill_damage=skill_damage, modifier=stats_dict["AD"], target=target, damage_type=DamageType.physical)

def knife_throw_func(stats_dict, target):
    skill_damage = 4
    apply_damage(skill_damage=skill_damage, modifier=stats_dict["AD"], target=target, damage_type=DamageType.physical)
    