from DamageCalculations.Type import DamageType
Cleric_stats_dict = {
    "max_hp": 100,
    "attack_damage": 5,
    "ability_power": 10,
    "resistance": {DamageType.physical: 5, DamageType.elemental: 10, DamageType.holy: 100, DamageType.dark: 5}
    }