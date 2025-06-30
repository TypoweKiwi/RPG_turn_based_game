from enum import Enum
from Skills.Skills_func import heal_func, holy_smite_func, prayer_func

class Skill_type:
    SINGLE_TARGET = 1
    AOE = 2
    SELF_CAST = 3


holy_smite_dict = {
    "name": "Holy smite",
    "func": holy_smite_func,
    "cost": 30,
    "desc": "Smite single enemy with powerful holy thunder",
    "skill_type": Skill_type.SINGLE_TARGET
}

heal_dict = {
    "name": "Heal",
    "func": heal_func,
    "cost": 20,
    "desc": "Heal ability recovers player HP",
    "skill_type": Skill_type.SELF_CAST
}


prayer_dict = {
    "name": "Prayer",
    "func": prayer_func,
    "cost": 40,
    "desc": "Pray for divine intervention on your enemies",
    "skill_type": Skill_type.AOE
}