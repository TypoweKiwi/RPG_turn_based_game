import json
import os
from Game.Choices_func import make_query

def return_save_name(save_name):
    save_parts = save_name.split(".")
    return "Team: " + save_parts[1] + " Date: " + save_parts[2]

def create_skill_dict(skill):
    return {
        "name": skill.name,
        "cost": skill.cost,
        "cost_type": skill.cost_type.name,
        "desc": skill.desc,
        "skill_type": skill.skill_type.name,
        "n_targets": skill.n_targets,
        "dmg_type": skill.damage_type.name,
        "scaling": skill.scaling,
        "effect": skill.effect,
        "crit": skill.crit
    }

def create_skills_dict(player):
    skills = player.skills
    skill_dict = {"n_skills": len(skills)}
    for i, skill in enumerate(skills):
        skill_dict[i] = create_skill_dict(skill)
    return skill_dict


def create_player_dict(player): #We save all atributes, but we will use only atributes that change like HP or MP.
    return {                    #Later in game there will be added items affecting atributes like MAX_HP, that why we save atributes we will not be using in current game state loader.
        "name": player.name,
        "max_hp": player.max_hp,
        "max_mp": player.max_mp,
        "mana_points": player.mana_points,
        "max_stamina": player.max_stamina,
        "stamina": player.stamina,
        "attack_damage": player.attack_damage,
        "critical_chance": player.critical_chance,
        "ability_power": player.ability_power,
        "speed": player.speed,
        "resistance": player.resistance,
        "skills": create_skills_dict(player)
    }

def create_map_dict(map): #Similiar to create_player_dict we save max_steps and safe_zones for possible further applications.
    return {                
        "current_position": map.current_position,
        "max_steps": map.max_steps,
        "safe_zones": map.safe_zones
    }

def save_game(save_path, saver_folder_path, players, map):
    save_dict = {"n_players": len(players)}
    for i, player in enumerate(players):
        save_dict[i] = create_player_dict(player)

    save_dict["map"] = create_map_dict(map)

    saves_list = [name for name in os.listdir(saver_folder_path) if name.endswith(".txt")]
    if len(saves_list) >= 7:
        choices = []
        for name in saves_list:
            choices.append({"name": return_save_name(name), "value": name})
        choice = make_query(message="\nWhich save do you wish to overwrite?", choices=choices)
        os.remove(os.path.join(saver_folder_path, choice))

    with open(save_path, "w") as file:
        json.dump(save_dict, file)

def Load_game():
    pass


