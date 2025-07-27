import random
#TODO BALANCE - Basic stats dict - skill damage - skill resistacne

def apply_damage(stats_dict, target, skill_dict, criticality=False):
    scaling_dict = skill_dict["scalling"]
    base = scaling_dict["base"]
    modifier = stats_dict[scaling_dict["type"]]
    damage_type = skill_dict["dmg_type"]
    crit_chance = stats_dict.get("Crit", 0)

    damage = base*modifier
    if criticality:
        ticket = random.random() 
        damage = damage*2 if crit_chance >= ticket else damage
    target.take_hit(damage, damage_type)

def basic_attack_func(stats_dict, target, skill_dict):
    apply_damage(stats_dict, target, skill_dict, criticality=skill_dict["crit"])

def holy_smite_func(stats_dict, target, skill_dict):
    apply_damage(stats_dict, target, skill_dict)

def heal_func(stats_dict, target, skill_dict):
    scalling_dict = skill_dict["scalling"]
    ability_power = stats_dict[scalling_dict["type"]]
    base = scalling_dict["base"]
    heal_amount = base*int(ability_power*scalling_dict["factor"])
    target.health_points = min(target.max_hp, target.health_points + heal_amount)
    print(f"{target.name} was healed {heal_amount} HP")

def prayer_func(stats_dict, targets, skill_dict):
    for target in targets:
        apply_damage(stats_dict, target, skill_dict)

def barbaric_charge_func(stats_dict, targets, skill_dict):
    for target in targets:
        apply_damage(stats_dict, target, skill_dict)

def heavy_strike_func(stats_dict, target, skill_dict):
    stats_dict["Crit"] = stats_dict["Crit"]/2
    apply_damage(stats_dict, target, skill_dict, criticality=skill_dict["crit"])

def battle_cry_func(stats_dict, targets, skill_dict): 
    for target in targets:
        apply_damage(stats_dict, target, skill_dict)

def knife_throw_func(stats_dict, target, skill_dict):
    apply_damage(stats_dict, target, skill_dict)
    