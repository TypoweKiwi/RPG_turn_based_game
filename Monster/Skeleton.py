from PlayerClasses.Player import Player
from Monster.Basic_stats import skeleton_stats_dict

class Skeleton(Player):
    def __init__(self, name="Skeleton", basic_stat_dict=skeleton_stats_dict):
        super().__init__(name, basic_stat_dict)
