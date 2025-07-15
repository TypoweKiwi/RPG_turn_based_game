from DamageCalculations.Type import DamageType

cleric_stats_dict = {
    "max_hp": 100,
    "max_mp": 60,
    "attack_damage": 5,
    "ability_power": 15,
    "crit_chance": 0,
    "speed": 4,
    "resistance": {
        DamageType.physical: 10,
        DamageType.elemental: 10,
        DamageType.holy: 80,
        DamageType.dark: 10
    }
}

barbarian_stats_dict = {
    "max_hp": 180,
    "max_mp": 0,
    "attack_damage": 18,
    "ability_power": 0,
    "crit_chance": 20,
    "speed": 3,
    "resistance": {
        DamageType.physical: 20,
        DamageType.elemental: 10,
        DamageType.holy: 10,
        DamageType.dark: 10
    }
}

fighter_stats_dict = {
    "max_hp": 120,
    "max_mp": 40,
    "attack_damage": 14,
    "ability_power": 5,
    "crit_chance": 20,
    "speed": 5,
    "resistance": {
        DamageType.physical: 30,
        DamageType.elemental: 5,
        DamageType.holy: 5,
        DamageType.dark: 5
    }
}

wizard_stats_dict = {
    "max_hp": 80,
    "max_mp": 80,
    "attack_damage": 5,
    "ability_power": 22,
    "crit_chance": 0,
    "speed": 6,
    "resistance": {
        DamageType.physical: 5,
        DamageType.elemental: 20,
        DamageType.holy: 5,
        DamageType.dark: 20
    }
}

rogue_stats_dict = {
    "max_hp": 80,
    "max_mp": 40,
    "attack_damage": 12,
    "ability_power": 0,
    "crit_chance": 40,
    "speed": 7,
    "resistance": {
        DamageType.physical: 5,
        DamageType.elemental: 5,
        DamageType.holy: 5,
        DamageType.dark: 5
    }
}

archer_stats_dict = {
    "max_hp": 90,
    "max_mp": 40,
    "attack_damage": 14,
    "ability_power": 5,
    "crit_chance": 35,
    "speed": 7,
    "resistance": {
        DamageType.physical: 10,
        DamageType.elemental: 10,
        DamageType.holy: 5,
        DamageType.dark: 5
    }
}


