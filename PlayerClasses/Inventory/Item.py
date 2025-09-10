from PlayerClasses.Stats import Stats

class Item:
    def __init__(self, item_stats_dict, prefix_dict, level=1, rarity=""):
        self.name = item_stats_dict["name"]
        self.desc = item_stats_dict["desc"]
        self.stats = Stats(item_stats_dict["basic_stat_dict"], level)
        self.slot = item_stats_dict["slot"]
        self.block_off_hand = item_stats_dict.get("block_off_hand", False)

        #Prefix and rarity
        self.rarity = rarity
        self.prefix_name = prefix_dict["name"]
        self.prefix_stats = Stats(prefix_dict["basic_stat_dict"], level)

    def get_name(self):
        return self.prefix_name + self.name
    
    def get_stats_to_calculate(self):
        return (self.stats + self.prefix_stats)
    