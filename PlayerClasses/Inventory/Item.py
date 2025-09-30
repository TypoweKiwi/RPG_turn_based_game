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
    def __init__(self, item_stats_dict, prefix_dict={}, level=1, rarity="Base"):
        self.name = item_stats_dict.get("name", "")
        self.desc = item_stats_dict.get("desc", "")
        self.stats = Stats(item_stats_dict.get("basic_stat_dict", {}), level)
        self.slot = item_stats_dict.get("slot", "")
        self.block_off_hand = item_stats_dict.get("block_off_hand", False)
        self.level = level
        self.max_upgrade_level = 3
        self.upgrade_counter = 0

        #Prefix and rarity
        self.rarity = rarity
        self.rarity_color = rarity_colors[rarity]
        self.prefix_name = prefix_dict.get("name", "")
        self.prefix_stats = Stats(prefix_dict.get("basic_stat_dict", {}), level)

        #Item price
        self.price = self.calculate_price(self.level)
        self.base_price = self.price #Base price will be helpfull for shop, to recover orginal price after item is bought
    
    def calculate_price(self, level):
        base = 300
        return base*rarity_factors[self.rarity]*(level**1.2)
    
    def update_item(self, level):
        self.level = level
        self.stats.update_stats(level)
        self.prefix_stats.update_stats(level)
        self.price = self.calculate_price(level)
        self.base_price = self.price
    
    def upgrade(self):
        self.update_item(self.level + 1)
        self.upgrade_counter += 1

    def get_item_panel(self, shop=False):
        desc = self.desc
        stats_str = "\n" + self.get_item_stats_str()
        gold_value_str = f"\n[yellow]Gold value[/yellow]: {self.price}" if not shop else f"\n[yellow]Price[/yellow]: {self.price}"
        upgraded_str = f"\n[dark_magenta]Upgrades[/dark_magenta]: {self.upgrade_counter}/{self.max_upgrade_level}" if not shop else ""
        panel_content = (desc  + stats_str +  upgraded_str + gold_value_str)
        item_panel = Panel((panel_content), title=f"[{self.rarity_color}]{self.get_name()}[/{self.rarity_color}]")
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
        return self.prefix_stats.get_item_stats_str()
    
    def __repr__(self):
        return self.get_name()
    
    def __eq__(self, other):
        return isinstance(other, Item) and self.__dict__ == other.__dict__
    
    def to_save_dict(self):
        save_dict = self.__dict__.copy()
        save_dict["stats"] = self.stats.to_save_dict()
        save_dict["prefix_stats"] = self.prefix_stats.to_save_dict()
        return save_dict
    
    def load_save_dict(self, save_dict):
        self.name = save_dict["name"]
        self.desc = save_dict["desc"]
        self.stats.load_save_dict(save_dict["stats"])
        self.slot = save_dict["slot"]
        self.block_off_hand = save_dict["block_off_hand"]
        self.level = save_dict["level"]
        self.max_upgrade_level = save_dict["max_upgrade_level"]
        self.upgrade_counter = save_dict["upgrade_counter"]
        self.rarity = save_dict["rarity"]
        self.rarity_color = save_dict["rarity_color"]
        self.prefix_name = save_dict["prefix_name"]
        self.prefix_stats.load_save_dict(save_dict["prefix_stats"])
        self.price = save_dict["price"]
        self.base_price = save_dict["base_price"]