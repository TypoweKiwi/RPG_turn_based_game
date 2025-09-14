from Game.UI.Choices_func import make_query, show_message
from PlayerClasses.Inventory.Item_and_affixes_lists.armor_list import ItemType
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
        self.equip_action_dict = {
            ItemType.ring.name: self.equip_ring,
            ItemType.main_hand.name: self.equip_main_hand,
            ItemType.off_hand.name: self.equip_off_hand,
        }
        self.temporary_stash = []

    def transfer_to_stash(self, stash):
        for item in self.temporary_stash:
            stash.add_item(item)
        self.temporary_stash = []

    def equip_item(self, item, stash):
        action = self.equip_action_dict.get(item.slot, self.equip_item_on_slot)
        action(item)
        self.transfer_to_stash(stash)
    
    def take_item_off(self, slot, stash):
        self.get_item(slot)
        self.transfer_to_stash(stash)

    def get_item(self, slot):
        removed_item = self.inventory_dict[slot]
        self.inventory_dict[slot] = None
        self.temporary_stash.append(removed_item) if removed_item is not None else None 
    
    def equip_ring(self, item):
        message = "On which slot do you wish to wear the ring?"
        choices = [{"name": "Ring", "value": ItemType.ring.name}, {"name": "Second ring", "value": "Second" + ItemType.ring.name}]
        slot = make_query(message=message, choices=choices)
        self.equip_item_on_slot(item, slot)
    
    def equip_main_hand(self, item):
        if item.block_off_hand and self.inventory_dict[ItemType.off_hand.name] is not None:
            show_message("Off-hand item removed because you equipped a two-handed weapon")
            self.get_item(ItemType.off_hand.name)
        self.equip_item_on_slot(item, item.slot)
    
    def equip_off_hand(self, item):
        main_item = self.inventory_dict[ItemType.main_hand.name]
        if main_item and main_item.block_off_hand:
            show_message("You cannot equip an off-hand item while wielding a two-handed weapon")
            self.temporary_stash.append(item)
        else:
            self.equip_item_on_slot(item, item.slot)

    def equip_item_on_slot(self, item, slot=None): #We need slot as another argument becasue of ring handling
        slot = item.slot if slot is None else slot
        self.get_item(slot)
        self.inventory_dict[slot] = item

    def get_inventory_stats(self):
        sum_stats = Stats(basic_stat_dict={}) #This will give blank stats object
        for key in self.inventory_dict:
            if not self.inventory_dict[key] == None:
                sum_stats += self.inventory_dict[key].get_stats_to_calculate()
        return sum_stats
    

