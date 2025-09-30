from PlayerClasses.Inventory.Item_and_affixes_lists.prefixes_list import common_prefixes_lst, uncommon_prefixes_lst, rare_prefixes_lst, epic_prefixes_lst, legendary_prefixes_lst
from PlayerClasses.Inventory.Item_and_affixes_lists.armor_list import armor_templates_list
from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import weapon_templates_list
from PlayerClasses.Inventory.Item import Item
import random

rarity_affix = { #We define this dict outside class bacuse it will be used in another file (Stash)
    "Base": common_prefixes_lst,
    "Uncommon": uncommon_prefixes_lst,
    "Rare": rare_prefixes_lst,
    "Epic": epic_prefixes_lst,
    "Legendary": legendary_prefixes_lst
}

class Item_generator:
    def __init__(self):
        self.rarity_affix = rarity_affix

        self.difficulty_table = { #For each of four difficulties there will be diffrent rewards -> (rarities, weights)
            "short" : (["Base", "Uncommon", "Rare"], [0.5, 0.3, 0.2,]),
            "medium": (["Base", "Uncommon", "Rare", "Epic"], [0.2, 0.45, 0.3, 0.05]),
            "long": (["Uncommon", "Rare", "Epic", "Legendary"], [0.2, 0.45, 0.3, 0.05]),
            "boss": (["Rare", "Epic", "Legendary"], [0.25, 0.55, 0.2]),
            "shop": (["Base", "Uncommon", "Rare", "Epic", "Legendary"],[0.4, 0.3, 0.2, 0.08, 0.02]) #There is also a seperate for shop loot table (only used by shop class)
        }

    def generate_item(self, difficulty_key, level, templates=(armor_templates_list + weapon_templates_list)):
        rarity_table = self.difficulty_table[difficulty_key]
        rarity = random.choices(rarity_table[0], weights=rarity_table[1], k=1)[0]
        prefixes_lst = self.rarity_affix[rarity]
        prefix_dict = random.choice(prefixes_lst)
        item_dict = random.choice(templates)
        return Item(
            item_stats_dict=item_dict, 
            level=level, 
            rarity=rarity, 
            prefix_dict=prefix_dict
        )

    def generate_weapon(self, difficulty_key, level, templates=weapon_templates_list):
        return self.generate_item(difficulty_key, level, templates)

    def generate_armor(self, difficulty_key, level, templates=armor_templates_list):
        return self.generate_item(difficulty_key, level, templates)
    
    def __eq__(self, other):
        return isinstance(other, Item_generator) and self.__dict__ == other.__dict__

