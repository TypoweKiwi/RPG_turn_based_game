class Item:
    def __init__(self, item_stats_dict):
        self.name = item_stats_dict["name"]
        self.desc = item_stats_dict["desc"]
        self.max_hp = item_stats_dict["max_hp"]
        self.max_mp = item_stats_dict["max_mp"]
        self.max_stamina = item_stats_dict["max_stamina"]
        self.attack_damage = item_stats_dict["attack_damage"]
        # self.critical_chance = item_stats_dict["critical_chance"] #for balance reasons items will not affect crit chance (IMO it should be only class oriented atrribute)
        self.ability_power = item_stats_dict["ability_power"]
        self.speed = item_stats_dict["speed"]
        self.resistance = item_stats_dict["resistance"]
        self.slot = item_stats_dict["slot"]