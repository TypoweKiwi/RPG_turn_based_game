from enum import Enum
import Skills.Skills_func
from DamageCalculations.Type import DamageType

class Skill_type(Enum):
    SINGLE_TARGET = "Single target"
    AOE = "Area of effect"
    SELF_CAST = "Self cast"
    TEAM_CAST = "Team cast"

class Skill_cost_type(Enum):
    MP = "MP"
    Stamina = "Stamina"
    HP = "HP"

basic_attack_dict = {
    "name": "Basic attack",
    "func": Skills.Skills_func.basic_attack_func,
    "cost": 0,
    "cost_type": Skill_cost_type.Stamina,
    "desc": "Strike the enemy with your weapon.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1,
    "scaling": {"type": "AD", "base": 1},
    "effect": "damage",
    "dmg_type": DamageType.physical,
    "crit": True
}


holy_smite_dict = {
    "name": "Holy smite",
    "func": Skills.Skills_func.holy_smite_func,
    "cost": 30,
    "cost_type": Skill_cost_type.MP,
    "desc": "Call down holy thunder on one enemy.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1,
    "scaling": {"type": "AP", "base": 4},
    "effect": "damage",
    "dmg_type": DamageType.holy,
    "crit": False
}

heal_dict = {
    "name": "Heal",
    "func": Skills.Skills_func.heal_func,
    "cost": 20,
    "cost_type": Skill_cost_type.MP,
    "desc": "Restore health to a single ally.",
    "skill_type": Skill_type.TEAM_CAST,
    "n_targets": 1,
    "scaling": {"type": "AP", "base": 3, "factor": 0.7},
    "effect": "heal",
    "dmg_type": DamageType.holy,
    "crit": False
}


prayer_dict = {
    "name": "Prayer",
    "func": Skills.Skills_func.prayer_func,
    "cost": 40,
    "cost_type": Skill_cost_type.MP,
    "desc": "Smite multiple enemies with divine power.",
    "skill_type": Skill_type.AOE,
    "n_targets": 3,
    "scaling": {"type": "AP", "base": 3},
    "effect": "damage",
    "dmg_type": DamageType.holy,
    "crit": False
}

barbaric_charge_dict = {
    "name": "Barbaric charge",
    "func": Skills.Skills_func.barbaric_charge_func,
    "cost": 20,
    "cost_type": Skill_cost_type.HP,
    "desc": "Charge wildly, hitting multiple enemies with force.",
    "skill_type": Skill_type.AOE,
    "n_targets": 3,
    "scaling": {"type": "AD", "base": 3},
    "effect": "damage",
    "dmg_type": DamageType.physical,
    "crit": False
}

heavy_strike_dict = {
    "name": "Heavy strike",
    "func": Skills.Skills_func.heavy_strike_func,
    "cost": 25,
    "cost_type": Skill_cost_type.Stamina,
    "desc": "Deliver a powerful blow to one target.",
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1,
    "scaling": {"type": "AD", "base": 2},
    "effect": "damage",
    "dmg_type": DamageType.physical,
    "crit": True
}

battle_cry_dict = { #TODO lesser scaling and armor debuff, add to desc how many armor debuff (hard stack value)
    "name": "Battle cry",
    "func": Skills.Skills_func.battle_cry_func,
    "cost": 30,
    "cost_type": Skill_cost_type.Stamina,
    "desc": "Roar damages and weakens all nearby enemies.",
    "skill_type": Skill_type.AOE,
    "n_targets": 4,
    "scaling": {"type": "AD", "base": 3},
    "effect": "Armor shredding",
    "dmg_type": DamageType.physical,
    "crit": True
}

knife_throw_dict = { #TODO ignoring enemy armor in skill func, add to desc how many armor ignored (hard stack value)
    "name": "Knife throw",
    "func": Skills.Skills_func.knife_throw_func,
    "cost": 15,
    "cost_type": Skill_cost_type.Stamina,
    "desc": "Throw a knife that pierces enemy defenses.", 
    "skill_type": Skill_type.SINGLE_TARGET,
    "n_targets": 1,
    "scaling": {"type": "AD", "base": 4},
    "effect": "damage",
    "dmg_type": DamageType.physical,
    "crit": False
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
