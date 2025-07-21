from enum import Enum
import Skills.Skills_func

class Skill_type(Enum):
    SINGLE_TARGET = 1
    AOE = 2
    SELF_CAST = 3

basic_attack_dict = {
    "name": "Basic attack",
    "func": Skills.Skills_func.basic_attack_func,
    "cost": 0,
    "desc": "Strike enemy with your weapon",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}


holy_smite_dict = {
    "name": "Holy smite",
    "func": Skills.Skills_func.holy_smite_func,
    "cost": 30,
    "desc": "Smite single enemy with powerful holy thunder",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1
}

heal_dict = {
    "name": "Heal",
    "func": Skills.Skills_func.heal_func,
    "cost": 20,
    "desc": "Heal ability recovers player HP",
    "skill_type": Skill_type.SELF_CAST,
    "n_targets": 1
}


prayer_dict = {
    "name": "Prayer",
    "func": Skills.Skills_func.prayer_func,
    "cost": 40,
    "desc": "Pray for divine intervention on your enemies",
    "skill_type": Skill_type.AOE,
    "n_targets": 3
}

skill_list = [
    holy_smite_dict,
    heal_dict,
    prayer_dict
]
