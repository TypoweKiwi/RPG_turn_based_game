from Game.Game import Game
from Game.AdventureHub.AdventureHub import AdventureHub
from PlayerClasses.Team import Team
from PlayerClasses.Classes import classes
from PlayerClasses.Inventory.Item import Item
from PlayerClasses.Inventory.Item_and_affixes_lists.weapons_list import viking_shield_dict, viking_axe_dict
from PlayerClasses.Inventory.Item_and_affixes_lists.prefixes_list import worn_dict, mighty_dict


#Item creeation
viking_axe = Item(item_stats_dict=viking_axe_dict, prefix_dict=worn_dict)
viking_shield = Item(item_stats_dict=viking_shield_dict, prefix_dict=mighty_dict, rarity="Rare")

#Player creation
cleric  = classes["Cleric"]()
barbarian = classes["Barbarian"]()

#Player diffrent levels -> player diffrent stats
cleric.gain_exp(1000)
barbarian.gain_exp(1500)

#Diffrent inventories
cleric.inventory.equip_item(viking_axe, [])
barbarian.inventory.equip_item(viking_shield, [])

#Creation of team/Adding players to team
team = Team(name="Test")
team.add_player(cleric)
team.add_player(barbarian)

#Adding items to stash/Adding gold to wallet
team.stash.add_item(viking_axe)
team.stash.add_item(viking_shield)
team.stash.wallet.earn(1000)

#Saving our syntetic game
game1 = Game()
game1.adventure_hub = AdventureHub(team=team)
game1.save_game_state()

#Loading our syntetic game
game2 = Game()
game2.load_game_state()

#Comparing both games
if game1.adventure_hub == game2.adventure_hub:
    print("Test passed")
else:
    print("Test failed")