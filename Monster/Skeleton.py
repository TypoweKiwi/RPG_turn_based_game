from PlayerClasses.Player import Player
from Monster.Basic_stats import skeleton_stats_dict
from Skills.Skills_list import basic_attack_dict
from Skills.Skill import Skill

class Skeleton(Player):
    def __init__(self, name="Skeleton", basic_stat_dict=skeleton_stats_dict, hostile=True):
        super().__init__(name, basic_stat_dict, hostile)

        self.skills = [
            Skill(basic_attack_dict)
            ]
