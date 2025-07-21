from PlayerClasses.Player import Player
from Skills.Skill import Skill
from Skills.Skills_list import basic_attack_dict
from PlayerClasses.Basic_stats import barbarian_stats_dict

class Barbarian(Player): #TODO barbarian skills 
    def __init__(self, name="Barbarian", basic_stat_dict=barbarian_stats_dict):
        super().__init__(name, basic_stat_dict)

        self.skills = [
            Skill(basic_attack_dict),
        ]
    