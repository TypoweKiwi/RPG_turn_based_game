from PlayerClasses.Inventory.Item_and_affixes_lists.armor_list import DamageType, ItemType



viking_axe_dict = {
    "name": "Viking axe",
    "desc": "A simple but deadly axe used by northern warriors",
    "slot": ItemType.main_hand.name,
    "basic_stat_dict": {
        "max_hp" : 5,
        "attack_damage": 10
    }
}

viking_double_axe_dict = {
    "name": "Viking double axe",
    "desc": "A massive two-handed axe forged for sheer destruction",
    "slot": ItemType.main_hand.name,
    "block_off_hand": True,
    "basic_stat_dict": {
        "max_hp" : 10,
        "attack_damage": 20
    }
}

viking_shield_dict = {
    "name": "Viking round shield",
    "desc": "A sturdy wooden shield reinforced with iron",
    "slot": ItemType.off_hand.name,
    "basic_stat_dict": {
        "max_hp" : 10,
        "resistance" : {DamageType.physical.name: 10}
    }
}

holy_bible_dict = {
    "name": "Holy bible",
    "desc": "A sacred book filled with divine scriptures",
    "slot": ItemType.main_hand.name,
    "basic_stat_dict": {
        "ability_power": 10,
        "resistance" : {DamageType.dark.name: 5}
    }
}

priest_thurible_dict = {
    "name": "Priest thurible",
    "desc": "A metal censer used during holy rituals",
    "slot": ItemType.off_hand.name,
    "basic_stat_dict": {
        "max_mp": 15
    }
}

priest_staff_dict = {
    "name": "Priest staff",
    "desc": "A tall wooden staff adorned with holy carvings",
    "slot": ItemType.main_hand.name,
    "block_off_hand": True,
    "basic_stat_dict": {
        "ability_power": 20,
        "max_mp": 10
    }
}


weapon_templates_list = {
    viking_axe_dict,
    viking_double_axe_dict,
    viking_shield_dict,
    holy_bible_dict,
    priest_thurible_dict,
    priest_staff_dict
}