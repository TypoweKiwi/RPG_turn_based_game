from PlayerClasses.Inventory.Item import Item
from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import viking_shield_dict, viking_axe_dict
from PlayerClasses.Inventory.Item_and_affixes_lists.prefixes_list import worn_dict
from PlayerClasses.Team import Team
from Game.UI.HubUI import HubUI
from Game.UI.Choices_func import show_message
from PlayerClasses.Classes import classes


viking_axe = Item(item_stats_dict=viking_axe_dict, prefix_dict=worn_dict)
viking_shield = Item(item_stats_dict=viking_shield_dict, prefix_dict=worn_dict)

team = Team(name="Test")
team.add_player(classes["Cleric"]())
team.stash.add_item(viking_axe)
team.stash.add_item(viking_shield)

hub_ui = HubUI(team=team)
hub_ui.view_items()

show_message(str(team._players[0].inventory.inventory_dict))


