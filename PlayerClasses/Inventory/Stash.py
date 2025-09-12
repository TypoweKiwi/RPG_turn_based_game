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
    
    def exit_view_panel(self):
        self.view_status = False
    
    def next_page(self):
        if self.stop < len(self.filtered_items):
            self.start += self.n_items_to_view
            self.stop = min(self.stop + self.n_items_to_view, len(self.filtered_items))

    def previous_page(self):
        if self.start > 0:
            self.start -= self.n_items_to_view
            self.stop = self.start + self.n_items_to_view
    
    def view_items(self):
        message = "\nChoose item to inspect/equip: "
        self.view_status = True
        self.start = 0
        self.stop = min(self.n_items_to_view, len(self.filtered_items))
        while self.view_status:
            choices = [{"name": f"{i+1}. {self.filtered_items[i].get_name()}", "value": (self.item_options, self.filtered_items[i])} for i in range(self.start, self.stop)]
            choices.append({"name": "Next page", "value": (self.next_page, None)})
            choices.append({"name": "Previous page", "value": (self.previous_page, None)})
            choices.append({"name": "Back", "value": (self.exit_view_panel, None)})
            choice = make_query(message=message, choices=choices)
            func, arg = choice
            func(arg) if arg else func()

    def item_options(self, item):
        pass