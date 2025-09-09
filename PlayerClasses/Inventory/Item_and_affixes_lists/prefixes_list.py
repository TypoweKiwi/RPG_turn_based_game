from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import DamageType
#----------------------------------------------------------------Common

worn_dict = {
    "name": "Worn ",
    "basic_stat_dict": {}
}
old_dict = {
    "name": "Old ",
    "basic_stat_dict": {}
}

cracked_dict = {
    "name": "Cracked ",
    "basic_stat_dict": {}
}

plain_dict = {
    "name": "Plain ",
    "basic_stat_dict": {}
}

common_prefixes_lst = [
    worn_dict,
    old_dict,
    cracked_dict,
    plain_dict
]

#----------------------------------------------------------------UNCOMMON

sturdy_dict = {
    "name": "Sturdy ",
    "basic_stat_dict": {
        "max_hp": 10,
        "resistance": {DamageType.physical.name: 3}
    }
}

swift_dict = {
    "name": "Swift ",
    "basic_stat_dict": {
        "speed" : 2
    }
}

bright_dict = {
    "name": "Bright ",
    "basic_stat_dict": {
        "max_mp": 8
    }
}

keen_dict = {
    "name": "Keen ",
    "basic_stat_dict": {
        "critical_chance": 2
    }
}

balanced_dict = {
    "name": "Balanced ",
    "basic_stat_dict": {
        "max_hp": 5,
        "max_mp": 5,
        "speed": 1
    }
}

charged_dict = {
    "name": "Charged ",
    "basic_stat_dict": {
        "ability_power": 4
    }
}

sharp_dict = {
    "name": "Sharp ",
    "basic_stat_dict": {
        "attack_damage": 3
    }
}


uncommon_prefixes_lst = [
    sturdy_dict,
    swift_dict,
    bright_dict,
    keen_dict,
    balanced_dict,
    sharp_dict,
    charged_dict
]

#----------------------------------------------------------------RARE

mighty_dict = {
    "name": "Mighty ",
    "basic_stat_dict": {
        "attack_damage": 10
    }
}

arcane_dict = {
    "name": "Arcane ",
    "basic_stat_dict": {
        "ability_power": 12,
        "max_mp": 5
    }
}

vigorous_dict = {
    "name": "Vigorous ",
    "basic_stat_dict": {
        "max_stamina": 15,
        "max_hp": 5
    }
}

piercing_dict = {
    "name": "Piercing ",
    "basic_stat_dict": {
        "critical_chance": 5,
        "attack_damage": 3
    }
}

blessed_dict = {
    "name": "Blessed ",
    "basic_stat_dict": {
        "ability_power": 8,
        "resistance": {DamageType.holy.name: 10}
    }
}

rare_prefixes_lst = [
    mighty_dict,
    arcane_dict,
    vigorous_dict, 
    piercing_dict,
    blessed_dict
]

#----------------------------------------------------------------Epic

dark_forged_dict = {
    "name": "Dark forged ",
    "basic_stat_dict": {
        "attack_damage": 8,
        "ability_power": 8,
        "resistance": {DamageType.dark.name: 10}
    }
}

elemental_forged_dict = {
    "name": "Infernal ",
    "basic_stat_dict": {
        "attack_damage": 8,
        "ability_power": 8,
        "resistance": {DamageType.elemental.name: 10}
    }
}

divine_dict = {
    "name": "Divine ",
    "basic_stat_dict": {
        "attack_damage": 8,
        "ability_power": 8,
        "resistance": {DamageType.holy.name: 10}
    }
}

storm_forged_dict = {
    "name": "Storm forged ",
    "basic_stat_dict": {
        "ability_power": 12,
        "speed": 3,
        "resistance": {DamageType.elemental.name: 10}
    }
}

runed_dict = {
    "name": "Runed ",
    "basic_stat_dict": {
        "ability_power": 10,
        "max_mp": 15,
        "critical_chance": 3
    }
}

epic_prefixes_lst = [
    dark_forged_dict,
    elemental_forged_dict,
    divine_dict,
    storm_forged_dict,
    runed_dict
]

#----------------------------------------------------------------Legendary

dragonforged_dict = {
    "name": "Dragonforged ",
    "basic_stat_dict": {
        "attack_damage": 20,
        "max_hp": 30,
        "resistance": {
            DamageType.physical.name: 10,
            DamageType.elemental.name: 10
        }
    }
}

celestial_dict = {
    "name": "Celestial ",
    "basic_stat_dict": {
        "ability_power": 20,
        "max_mp": 30,
        "resistance": {
            DamageType.holy.name: 20,
            DamageType.dark.name: 10
        }
    }
}

worldbreaker_dict = {
    "name": "Worldbreaker ",
    "basic_stat_dict": {
        "attack_damage": 25,
        "critical_chance": 10,
        "speed": 5
    }
}

godslayer_dict = {
    "name": "Godslayer ",
    "basic_stat_dict": {
        "attack_damage": 15,
        "ability_power": 15,
        "critical_chance": 5,
        "resistance": {
            DamageType.holy.name: 10,
            DamageType.dark.name: 10
        }
    }
}

eternal_dict = {
    "name": "Eternal ",
    "basic_stat_dict": {
        "max_hp": 40,
        "max_mp": 20,
        "stamina": 15,
        "resistance": {
            DamageType.physical.name: 10,
            DamageType.elemental.name: 10,
            DamageType.holy.name: 10,
            DamageType.dark.name: 10
        }
    }
}

legendary_prefixes_lst = [
    dragonforged_dict,
    celestial_dict,
    worldbreaker_dict,
    godslayer_dict,
    eternal_dict
]