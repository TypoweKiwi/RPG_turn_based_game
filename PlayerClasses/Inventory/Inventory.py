from Game.UI.Choices_func import make_query
from PlayerClasses.Inventory.items_list import ItemType

class Inventory:
    def __init__(self):
        self.head = None #TODO change to dict self.slot_dict = {}
        self.chest = None
        self.legs = None
        self.boots = None 
        self.ring = None
        self.second_ring = None 
        self.necklace = None
        self.weapon = None #TODO Consider making primary and secondaty weapon -> heavy weapon need special handling

    def equip_item(self, item):
        slot = item.slot
        if slot == ItemType.ring:
            message = "On which slot do you wish to wear the ring?"
            choices = [{"name": "Ring", "value": "ring"}, {"name": "Second ring", "value": "second_ring"}]
            slot = make_query(message=message, choices=choices)    
        setattr(self, slot.value, item)
    
    def take_item_off(self):
        message = "From which slot you wish to take off item?"
        attr_dict = self.__dict__
        choices = [{"name": choice.capitalize().replace("_", " "), "value": choice} for choice in attr_dict.keys()]
        slot = make_query(message=message, choices=choices)
        removed_item = getattr(self, slot)
        setattr(self, slot, None)
        return removed_item