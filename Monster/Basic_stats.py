from DamageCalculations.Type import DamageType

skeleton_stats_dict = {
    "max_hp": 30,
    "max_mp": 5,
    "max_stamina": 30,
    "attack_damage": 6,
    "ability_power": 0,
    "critical_chance": 5,
    "speed": 6,
    "resistance": {
        DamageType.physical.name: 10,
        DamageType.elemental.name: 5,
        DamageType.holy.name: 0,
        DamageType.dark.name: 20
    }
}

armored_skeleton_stats_dict = {
    "max_hp": 60,
    "max_mp": 0,
    "max_stamina": 50,
    "attack_damage": 7,
    "ability_power": 0,
    "critical_chance": 0,
    "speed": 3,
    "resistance": {
        DamageType.physical.name: 40,
        DamageType.elemental.name: 10,
        DamageType.holy.name: -10,
        DamageType.dark.name: 30
    }
}

skeleton_archer_stats_dict = {
    "max_hp": 25,
    "max_mp": 0,
    "max_stamina": 40,
    "attack_damage": 10,
    "ability_power": 0,
    "critical_chance": 35,
    "speed": 7,
    "resistance": {
        DamageType.physical.name: 5,
        DamageType.elemental.name: 0,
        DamageType.holy.name: 0,
        DamageType.dark.name: 15
    }
}