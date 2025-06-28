from DamageCalculations.Type import DamageType

Cleric_stats_dict = {
    "max_hp": 80,
    "max_mp": 50,
    "attack_damage": 5,
    "ability_power": 10,
    "crit_chance": 0,
    "resistance": {DamageType.physical: 5, DamageType.elemental: 10, DamageType.holy: 100, DamageType.dark: 5}
    }


Barbarian_stats_dict = {
    "max_hp": 200,
    "max_mp": 0,
    "attack_damage": 20,
    "ability_power": 0,
    "crit_chance": 30,
    "resistance": {DamageType.physical: 10, DamageType.elemental: 10, DamageType.holy: 10, DamageType.dark: 10}
    }


Figter_stats_dict = {
    "max_hp": 100,
    "max_mp": 30,
    "attack_damage": 15,
    "ability_power": 5,
    "crit_chance": 30,
    "resistance": {DamageType.physical: 30, DamageType.elemental: 5, DamageType.holy: 5, DamageType.dark: 5}
    }


Wizard_stats_dict = {
    "max_hp": 70,
    "max_mp": 70,
    "attack_damage": 5,
    "ability_power": 20,
    "crit_chance": 0,
    "resistance": {DamageType.physical: 5, DamageType.elemental: 20, DamageType.holy: 5, DamageType.dark: 20}
    }

Rogue_stats_dict = {
    "max_hp": 80,
    "max_mp": 30,
    "attack_damage": 10,
    "ability_power": 0,
    "crit_chance": 50,
    "resistance": {DamageType.physical: 5, DamageType.elemental: 5, DamageType.holy: 5, DamageType.dark: 5}
    }


