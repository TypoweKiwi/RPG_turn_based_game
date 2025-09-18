from DamageCalculations.Type import DamageType

cleric_stats_dict = {
    "max_hp": 100,
    "max_mp": 60,
    "max_stamina": 40,
    "attack_damage": 5,
    "ability_power": 15, 
    "critical_chance": 0,
    "speed": 4,
    "resistance": {
        DamageType.physical.name: 10,
        DamageType.elemental.name: 10,
        DamageType.holy.name: 80,
        DamageType.dark.name: 10
    }
}

barbarian_stats_dict = {
    "max_hp": 180,
    "max_mp": 0,
    "max_stamina": 100,
    "attack_damage": 18,
    "ability_power": 0,
    "critical_chance": 20,
    "speed": 3,
    "resistance": {
        DamageType.physical.name: 20,
        DamageType.elemental.name: 10,
        DamageType.holy.name: 10,
        DamageType.dark.name: 10
    }
}

fighter_stats_dict = {
    "max_hp": 120,
    "max_mp": 40,
    "max_stamina": 80,
    "attack_damage": 14,
    "ability_power": 5,
    "critical_chance": 20,
    "speed": 5,
    "resistance": {
        DamageType.physical.name: 30,
        DamageType.elemental.name: 5,
        DamageType.holy.name: 5,
        DamageType.dark.name: 5
    }
}

wizard_stats_dict = {
    "max_hp": 80,
    "max_mp": 80,
    "max_stamina": 30,
    "attack_damage": 5,
    "ability_power": 22,
    "critical_chance": 0,
    "speed": 6,
    "resistance": {
        DamageType.physical.name: 5,
        DamageType.elemental.name: 20,
        DamageType.holy.name: 5,
        DamageType.dark.name: 20
    }
}

rogue_stats_dict = {
    "max_hp": 80,
    "max_mp": 40,
    "max_stamina": 60,
    "attack_damage": 12,
    "ability_power": 0,
    "critical_chance": 40,
    "speed": 7,
    "resistance": {
        DamageType.physical.name: 5,
        DamageType.elemental.name: 5,
        DamageType.holy.name: 5,
        DamageType.dark.name: 5
    }
}

archer_stats_dict = {
    "max_hp": 90,
    "max_mp": 40,
    "max_stamina": 70,
    "attack_damage": 14,
    "ability_power": 5,
    "critical_chance": 35,
    "speed": 7,
    "resistance": {
        DamageType.physical.name: 10,
        DamageType.elemental.name: 10,
        DamageType.holy.name: 5,
        DamageType.dark.name: 5
    }
}


