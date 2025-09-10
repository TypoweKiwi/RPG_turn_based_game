from PlayerClasses.Player import Player
from Monster.Basic_stats import skeleton_archer_stats_dict
from Skills.Skills_list import basic_attack_dict
from Skills.Skill import Skill

class Skeleton_archer(Player):
    def __init__(self, name="Skeleton archer", basic_stat_dict=skeleton_archer_stats_dict, hostile=True, level=1):
        super().__init__(name, basic_stat_dict, hostile, level=level)

        self.skills = [ #TODO skeleton archer skills
            Skill(basic_attack_dict)
            ]
