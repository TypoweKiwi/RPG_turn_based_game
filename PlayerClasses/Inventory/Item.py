from PlayerClasses.Stats import Stats
from rich.panel import Panel

rarity_colors = { #Colors will be neded in diffrent UI classes thats why we define it global and use it in item class
    "Base": "white",
    "Uncommon": "green",
    "Rare": "blue",
    "Epic": "magenta",
    "Legendary": "yellow"
}

rarity_factors = { 
    "Base": 1.0,
    "Uncommon": 1.6,
    "Rare": 2.8,
    "Epic": 5.0,
    "Legendary": 10.0
}

class Item:
    def __init__(self, item_stats_dict, prefix_dict, level=1, rarity="Base"):
        self.name = item_stats_dict["name"]
        self.desc = item_stats_dict["desc"]
        self.stats = Stats(item_stats_dict["basic_stat_dict"], level)
        self.slot = item_stats_dict["slot"]
        self.block_off_hand = item_stats_dict.get("block_off_hand", False)
        self.level = level

        #Prefix and rarity
        self.rarity = rarity
        self.rarity_color = rarity_colors[rarity]
        self.prefix_name = prefix_dict["name"]
        self.prefix_stats = Stats(prefix_dict["basic_stat_dict"], level)

        #Item price
        base = 300
        self.value = base*rarity_factors[rarity]*(level**1.2)
    
    def get_item_panel(self):
        desc = self.desc
        stats = self.get_item_stats_str()
        item_panel = Panel((desc + "\n" + stats + "\n" + f"Gold value: {self.price}"), title=f"[{self.rarity_color}]{self.get_name()}[/{self.rarity_color}]")
        return item_panel

    def get_name(self):
        return self.prefix_name + self.name
    
    def get_stats_to_calculate(self):
        return (self.stats + self.prefix_stats)
    
    def get_item_stats_str(self):
        return (self.stats + self.prefix_stats).get_item_stats_str()
    
    def get_item_raw_stats(self):
        return self.stats.get_item_stats_str()
    
    def get_prefix_raw_stats(self):
        return self.prefix_stats.get_item_stats_str
    
    def __repr__(self):
        return self.get_name()
    