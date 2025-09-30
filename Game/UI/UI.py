from Game.UI.Choices_func import make_query, choose_targets, show_message
from Skills.Skills_list import Skill_type
from rich.columns import Columns
from rich.console import Console

class UI:
    def __init__(self, team, enemies=None):
        self.team = team
        self.enemies = enemies
        
    def show_panel(self, panel):
        console = Console()
        with console.screen(style="on black"):
            console.print("\n")
            console.print(Columns(panel, expand=False, equal=False))
            show_message("")
    
    def show_vital_stats(self, player=None):
        return self.show_stats(player, resistance=False)

    def show_resistances(self, player=None):
        return self.show_stats(player, resistance=True)

    def show_stats(self, player, resistance):
        player_panels = self.team.player_stats_panel(resistance=resistance)
        enemy_panels = self.enemies.player_stats_panel(resistance=resistance) if self.enemies else None
        all_panels = player_panels + enemy_panels if self.enemies else player_panels
        self.show_panel(all_panels)
        return None
    
    def show_skills(self, player):
        skills_panels = player.get_skills_panel() 
        self.show_panel(skills_panels)
        return None