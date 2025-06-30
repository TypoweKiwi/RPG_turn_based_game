from DamageCalculations.Type import DamageType

skeleton_stats_dict = {
    "max_hp": 20,
    "max_mp": 0,
    "attack_damage": 5,
    "ability_power": 0,
    "crit_chance": 0,
    "resistance": {DamageType.physical: 10, DamageType.elemental: 10, DamageType.holy: 1, DamageType.dark: 15}
    }
