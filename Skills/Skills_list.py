from enum import Enum
import Skills.Skills_func

class Skill_type(Enum):
    SINGLE_TARGET = 1
    AOE = 2
    SELF_CAST = 3
    TEAM_CAST = 4

basic_attack_dict = {
    "name": "Basic attack",
    "func": Skills.Skills_func.basic_attack_func,
    "cost": 0,
    "desc": "Strike enemy with your weapon.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}


holy_smite_dict = {
    "name": "Holy smite",
    "func": Skills.Skills_func.holy_smite_func,
    "cost": 30,
    "desc": "Smite single enemy with powerful holy thunder.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}

heal_dict = {
    "name": "Heal",
    "func": Skills.Skills_func.heal_func,
    "cost": 20,
    "desc": "Heal ability recovers player HP.",
    "skill_type": Skill_type.TEAM_CAST,
    "n_targets": 1
}


prayer_dict = {
    "name": "Prayer",
    "func": Skills.Skills_func.prayer_func,
    "cost": 40,
    "desc": "Pray for divine intervention on your enemies.",
    "skill_type": Skill_type.AOE,
    "n_targets": 3
}

barbaric_charge_dict = {
    "name": "Barbaric charge",
    "func": Skills.Skills_func.barbaric_charge_func,
    "cost": 0,
    "desc": "A wild charge that strikes multiple foes with raw force",
    "skill_type": Skill_type.AOE,
    "n_targets": 3
}

heavy_strike_dict = {
    "name": "Heavy strike",
    "func": Skills.Skills_func.heavy_strike_func,
    "cost": 0,
    "desc": "A powerful blow focused on a single enemy.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}

battle_cry_dict = {
    "name": "Battle cry",
    "func": Skills.Skills_func.battle_cry_func,
    "cost": 0,
    "desc": "Unleash a thunderous roar that shakes the battlefield, damaging all nearby foes.",
    "skill_type": Skill_type.AOE,
    "n_targets": 4
}

knife_throw_dict = {
    "name": "Knife throw",
    "func": Skills.Skills_func.knife_throw_func,
    "cost": 0,
    "desc": "Throw a deadly knife with precision, piercing the target's defenses",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}


skill_list = [
    holy_smite_dict,
    heal_dict,
    prayer_dict,
    barbaric_charge_dict,
    heavy_strike_dict,
    battle_cry_dict,
    knife_throw_dict
]
