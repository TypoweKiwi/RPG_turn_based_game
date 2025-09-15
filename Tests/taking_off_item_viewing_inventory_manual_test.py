from PlayerClasses.Inventory.Item import Item
from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import viking_shield_dict, viking_axe_dict
from PlayerClasses.Inventory.Item_and_affixes_lists.prefixes_list import worn_dict, mighty_dict
from PlayerClasses.Team import Team
from Game.UI.HubUI import HubUI
from Game.UI.Choices_func import show_message
from PlayerClasses.Classes import classes


player = classes["Cleric"]()
viking_axe = Item(item_stats_dict=viking_axe_dict, prefix_dict=worn_dict)
viking_shield = Item(item_stats_dict=viking_shield_dict, prefix_dict=mighty_dict, rarity="Rare")

team = Team(name="Test")
team.add_player(player)
player.inventory.equip_item(viking_axe, team.stash)
player.inventory.equip_item(viking_shield, team.stash)

hubui = HubUI(team)
hubui.modify_player_inventory()

show_message(str(team.stash.items_list))