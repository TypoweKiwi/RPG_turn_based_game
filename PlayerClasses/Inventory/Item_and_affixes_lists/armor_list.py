from enum import Enum
from DamageCalculations.Type import DamageType

class ItemType(Enum):
    head = "head"
    chest = "chest"
    legs = "legs"
    boots = "boots"
    ring = "ring"
    necklace = "necklace"
    main_hand = "main_hand"
    off_hand = "off_hand"

viking_helmet_dict = {
    "name": "Viking helmet",
    "desc": "A sturdy iron helmet once worn by northern raiders",
    "slot": ItemType.head.name,
    "basic_stat_dict": {
        "max_hp" : 15,
        "resistance" : {DamageType.physical.name: 5}
    }
}

viking_chestplate_dict = {
    "name": "Viking chestplate",
    "desc": "A heavy chestplate reinforced with iron and leather",
    "slot": ItemType.chest.name,
    "basic_stat_dict": {
        "max_hp" : 25,
        "speed" : -1,
        "resistance" : {DamageType.physical.name: 10}
    }
}

viking_poleyns_dict = {
    "name": "Viking poleyns",
    "desc": "Iron knee guards crafted to withstand brutal strikes",
    "slot": ItemType.legs.name,
    "basic_stat_dict": {
        "max_hp" : 15,
        "resistance" : {DamageType.physical.name: 5}
    }
}

viking_boots_dict = {
    "name": "Viking fur boots",
    "desc": "Warm boots lined with fur",
    "slot": ItemType.boots.name,
    "basic_stat_dict": {
        "max_hp" : 10,
        "speed" : 1,
        "resistance" : {DamageType.physical.name: 2}
    }
}

priest_hat_dict = {
    "name": "Priest hat",
    "desc": "A simple hat blessed during holy rituals",
    "slot": ItemType.head.name,
    "basic_stat_dict": {
        "max_hp" : 5,
        "max_mp": 10,
        "resistance" : {DamageType.physical.name: 2, DamageType.holy.name: 2, DamageType.elemental.name: 2}
    }
}

priest_robe_dict = {
    "name": "Priest robe",
    "desc": "A robe infused with sacred symbols",
    "slot": ItemType.chest.name,
    "basic_stat_dict": {
        "max_hp" : 5,
        "max_mp": 10,
        "ability_power": 10,
        "resistance" : {DamageType.physical.name: 1, DamageType.holy.name: 2, DamageType.elemental.name: 5, DamageType.dark.name: -5}
    }
}

priest_crucifix_dict = {
    "name": "Priest crucifix",
    "desc": "Radiates holy energy and shields against darkness",
    "slot": ItemType.legs.name,
    "basic_stat_dict": {
        "max_mp": 10,
        "ability_power": 10,
        "resistance" : {DamageType.dark.name: 10}
    }
}

priest_sandals_dict = {
    "name": "Priest sandals",
    "desc": "",
    "slot": ItemType.boots.name,
    "basic_stat_dict": {
        "max_mp": 10,
        "speed": 3,
        "resistance" : {DamageType.physical.name: 5}
    }
}

armor_templates_list = [
    viking_helmet_dict,
    viking_chestplate_dict,
    viking_poleyns_dict,
    viking_boots_dict,
    priest_hat_dict,
    priest_robe_dict,
    priest_crucifix_dict,
    priest_sandals_dict,
]