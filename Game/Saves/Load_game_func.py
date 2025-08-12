import json
import os
from PlayerClasses.Classes import classes
from Skills.Skills_list import skill_list
from Skills.Skill import Skill
from PlayerClasses.Team import Team
from Game.Map import Map
from Game.Saves.Saves_game_func import save_path


def load_skill_dict(skill_dict):
    skill_lst = []
    for i in range(skill_dict["n_skills"]):
        skill_name = skill_dict[i]
        for element in skill_list:
            if skill_name == element["name"]:
                skill_list.append(Skill(element))
                break
    return skill_lst

def load_map_dict(map, map_dict, players):
    map.current_position = map_dict["current_position"]
    map.max_steps = map_dict["max_steps"]
    map.safe_zones = map_dict["safe_zones"]
    map.players = players

def load_game(save_name, save_path=save_path):
    save_name = save_name = os.path.join(save_path, save_name)
    with open(save_name, "r") as file:
        save_dict = json.load(file)
    
    players = Team(name=save_dict["team_name"])
    for i in range(save_dict["n_players"]):
        player = classes[save_dict["class"]]()
        player.update_from_dict(save_dict[i])
        players.add_player(player)
    
    map = Map()
    load_map_dict(map, save_dict["map"], players)

    return map