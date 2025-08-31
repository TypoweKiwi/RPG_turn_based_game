from Game.UI.Choices_func import make_query
from PlayerClasses.Inventory.items_list import ItemType
from PlayerClasses.Stats import Stats

class Inventory:
    def __init__(self):
        self.inventory_dict = {
            ItemType.head.name: None,
            ItemType.chest.name: None,
            ItemType.legs.name: None,
            ItemType.boots.name:None,
            ItemType.ring.name: None,
            "Second" + ItemType.ring.name: None,
            ItemType.necklace.name:None,
            ItemType.main_hand.name: None,
            ItemType.off_hand.name: None
        }

    def equip_item(self, item):
        slot = item.slot
        if slot == ItemType.ring:
            message = "On which slot do you wish to wear the ring?"
            choices = [{"name": "Ring", "value": ItemType.ring.name}, {"name": "Second ring", "value": "Second" + ItemType.ring.name}]
            slot = make_query(message=message, choices=choices)
        self.inventory_dict[slot.name] = item
    
    def take_item_off(self, slot):
        removed_item = self.inventory_dict[slot.name]
        self.inventory_dict[slot.name] = None
        return removed_item
    
    def get_inventory_stats(self):
        sum_stats = Stats(basic_stat_dict={}) #This will give blank stats object
        for key in self.inventory_dict():
            if not self.inventory_dict[key] == None:
                sum_stats += self.inventory_dict[key].stats
        return sum_stats