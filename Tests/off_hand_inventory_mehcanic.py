from PlayerClasses.Inventory.Inventory import Inventory
from PlayerClasses.Inventory.Item import Item
from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import viking_double_axe_dict, viking_shield_dict
from PlayerClasses.Inventory.Item_and_affixes_lists.prefixes_list import worn_dict
from PlayerClasses.Inventory.Stash import Stash

inventory_1 = Inventory()
inventory_2 = Inventory()
inventory_3 = Inventory()
inventory_4 = Inventory()
stash = Stash()
stash_2 = Stash()

double_handed_weapon = Item(item_stats_dict=viking_double_axe_dict, prefix_dict=worn_dict)
viking_shield_dict = Item(item_stats_dict=viking_shield_dict, prefix_dict=worn_dict)

inventory_1.equip_item(item=double_handed_weapon, stash=stash)
inventory_2.equip_item(item=double_handed_weapon, stash=stash)
inventory_2.equip_item(item=viking_shield_dict, stash=stash)

inventory_3.equip_item(item=double_handed_weapon, stash=stash_2)
inventory_4.equip_item(item=viking_shield_dict, stash=stash_2)
inventory_4.equip_item(item=double_handed_weapon, stash=stash_2)

if inventory_1.inventory_dict == inventory_2.inventory_dict and len(stash.items_list) == 1:
    print("Block off-hand mechaninc test passed")
else:
    print("Block off-hand mechaninc test failed")

if inventory_3.inventory_dict == inventory_4.inventory_dict and len(stash_2.items_list) == 1:
    print("Off hand item removing mechaninc test passed")
else:
    print("Off hand item removing mechaninc test failed")