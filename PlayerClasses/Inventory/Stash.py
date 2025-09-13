from PlayerClasses.Inventory.Item_and_affixes_lists.armor_list import ItemType
from PlayerClasses.Inventory.item_generator import rarity_affix
from PlayerClasses.Stats import scaling_pattern
from Game.UI.Choices_func import make_query, show_message

class Stash:
    def __init__(self):
        self.items_list = []
        self.filtered_items = self.items_list
        self.n_items_to_view = 5
        self.wallet = 0 #TODO add wallet class 
    
    def add_item(self, item):
        self.items_list.append(item)
    
    def get_item(self, idx):
        item = self.items_list[idx]
        self.items_list.remove(item)
        return item    

    def sort_stash(self):
        message = "\nWhat attribute would you like to sort/filtr stash by?"
        choices = [
            {"name": "Filter by item slot", "value": self.filter_by_slot},
            {"name": "Filter by item rarity", "value": self.filter_by_rarity},
            {"name": "Filter by item stats", "value": self.filter_by_stats},
            {"name": "Sort by item level", "value": self.sort_by_level},
            {"name": "Clear filter", "value": self.clear_filter},
            {"name": "Back", "value": lambda: None}
        ]
        choice = make_query(message, choices)
        choice()
    
    def filter_by_slot(self):
        message = "\nBy which slot you wish to filter items?"
        choices = [{"name": item.name.capitalize(), "value": item.name} for item in ItemType]
        slot = make_query(message, choices)
        self.filtered_items = [item for item in self.items_list if item.slot == slot]
    
    def filter_by_rarity(self):
        message = "\nBy which slot you wish to filter items?"
        choices = [{"name": rarity, "value": rarity} for rarity in rarity_affix]
        rarity = make_query(message, choices)
        self.filtered_items = [item for item in self.items_list if item.rarity == rarity]
    
    def filter_by_stats(self):
        message = "\nBy which stat you wish to filter items?"
        choices = [{"name": key.replace("_", " ").capitalize(), "value":key} for key in scaling_pattern]
        stat = make_query(message, choices)
        self.filtered_items = [item for item in self.items_list if item.stats.__dict__[stat] != 0]
    
    def sort_by_level(self):
        message = "\nIn which order you wish to sort items?"
        choices = [
            {"name": "Ascending", "value": False},
            {"name": "Descending", "value": True}
        ]
        reverse = make_query(message, choices)
        self.items_list.sort(key=lambda item: item.level, reverse=reverse)
        self.filtered_items = self.items_list

    def clear_filter(self):
        self.filtered_items = self.items_list