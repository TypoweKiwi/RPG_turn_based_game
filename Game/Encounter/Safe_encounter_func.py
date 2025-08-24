from Game.UI.Choices_func import show_message, make_query
from Skills.Skills_list import skill_list
from PlayerClasses.Classes import classes
import random

def fountain_of_life_func(players):
    heal_value = 50
    message = ""

    for player in players:
        player.health_points = min(player.max_hp, player.health_points+heal_value) #TODO change min to some healing function
        message += f"\n{player.name} current HP value {player.health_points}"
    message = f"\nYour team was healed." + message
    show_message(message=message)

def old_wizzard_func(players):
    skill_dict = random.choice(skill_list) 
    print(f"\nThe wizzard offer you to teach you {skill_dict['name']}")
    choice = make_query(message=f"Do you wish to learn {skill_dict['name']}", choices=["Yes", "No"]) 

    if choice == "Yes":
        player = make_query(message=f"On which character you wish to learn new skill?", choices=players)
        player.learn_skill(skill_dict)
    else:
        print("You decided turn down opportunity.")

def mana_source_func(players):
    mana_value = 50
    message = ""

    for player in players:
        player.mana_points = min(player.max_mp, player.mana_points+mana_value)
        message += f"\n{player.name} current MP value {player.mana_points}"
    message = f"\nYour team's mana has been restored" + message
    show_message(message=message)

def lost_adventurer_func(players):
    adventurer = random.choice(list(classes.keys()))
    print(f"\nYou've met {adventurer}.")
    choice = make_query(message="Do you wish to recruit him to your team?", choices=["Yes", "No"])
    if choice == "Yes":
        accepted = players.add_player(adventurer)
        if not accepted:
            print("You decided to let adventurer walk away.")
    else:
        print("You decided to let adventurer walk away.")
    
def town_func(players):
    heal_value = 30
    mana_value = 30
    message = ""
    for player in players:
        player.health_points = min(player.max_hp, player.health_points+heal_value)
        player.mana_points = min(player.max_mp, player.mana_points+mana_value)
        message += f"\n{player.name} current HP value {player.health_points} current MP value {player.mana_points}"
    message = f"\nYour team rested in local tavern." + message
    show_message(message=message)