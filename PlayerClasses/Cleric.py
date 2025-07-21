from PlayerClasses.Player import Player
from Skills.Skill import Skill
from Skills.Skills_list import holy_smite_dict, heal_dict, prayer_dict, basic_attack_dict
from PlayerClasses.Basic_stats import cleric_stats_dict

class Cleric(Player):
    def __init__(self, name="Cleric", basic_stat_dict=cleric_stats_dict):
        super().__init__(name, basic_stat_dict)

        self.skills = [
            Skill(basic_attack_dict), 
            Skill(holy_smite_dict),
            Skill(heal_dict),
            Skill(prayer_dict)
        ]
    