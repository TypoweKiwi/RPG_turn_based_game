from PlayerClasses.Player import Player
from Skills.Skill import Skill
from Skills.Skills_list import basic_attack_dict, heavy_strike_dict, barbaric_charge_dict, battle_cry_dict
from PlayerClasses.Basic_stats import barbarian_stats_dict

class Barbarian(Player):  
    def __init__(self, name="Barbarian", basic_stat_dict=barbarian_stats_dict):
        super().__init__(name, basic_stat_dict)

        self.skills = [
            Skill(basic_attack_dict),
            Skill(heavy_strike_dict),
            Skill(barbaric_charge_dict),
            Skill(battle_cry_dict)
        ]
    