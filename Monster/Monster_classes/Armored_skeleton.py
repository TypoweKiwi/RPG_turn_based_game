from PlayerClasses.Player import Player
from Monster.Basic_stats import armored_skeleton_stats_dict
from Skills.Skills_list import basic_attack_dict, heavy_strike_dict
from Skills.Skill import Skill

class Armored_skeleton(Player):
    def __init__(self, name="Armored skeleton", basic_stat_dict=armored_skeleton_stats_dict, hostile=True):
        super().__init__(name, basic_stat_dict, hostile)

        self.skills = [ #TODO armored skeleton skills
            Skill(basic_attack_dict),
            Skill(heavy_strike_dict)
            ]
