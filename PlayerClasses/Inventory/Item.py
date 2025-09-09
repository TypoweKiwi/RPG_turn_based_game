from PlayerClasses.Stats import Stats

class Item:
    def __init__(self, item_stats_dict, level=1, rarity="", rarity_factor=1, prefix="", prefix_stats_dict={}):
        self.name = item_stats_dict["name"]
        self.desc = item_stats_dict["desc"]
        self.stats = Stats(item_stats_dict, level)
        self.slot = item_stats_dict["slot"]
        self.block_off_hand = item_stats_dict.get("block_off_hand", False)

        #Prefix and rarity
        self.rarity = rarity
        self.prefix = prefix
        self.prefix_stats = Stats(prefix_stats_dict, level)

    def get_name(self):
        return self.rarity + self.prefix + self.name
    
    def get_stats_to_calculate(self):
        return (self.stats + self.prefix_stats)
    