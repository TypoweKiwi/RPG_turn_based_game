from rich.console import Console
from Game.UI.Choices_func import make_query, show_message
from rich.columns import Columns
from rich.panel import Panel

class HubUI:
    def __init__(self):
        pass
    
    def show_panel(self, panel):
        console = Console()
        with console.screen(style="on black"):
            console.print(Columns(panel, expand=False, equal=False))
            show_message("")

    def map_preset_comparission(self, presets):
        def get_preset_str(preset):
            return (
                f"[blue]Room numbers[/blue]: {preset['max_steps']}\n"
                f"[green]Safe room numbers[/green]: {preset['safe_zones_number']}\n"
                f"[red]Max enemies in room[/red]: {preset['max_enemies']}\n"
                f"[magenta]Boss[/magenta]: {preset['boss']}\n"
                f"[yellow]Gold cost[/yellow]: {preset['cost']}"
            )
        
        panel_lst = [Panel(get_preset_str(presets[key]), title=f"[cyan]{key.capitalize() + ' dungeon'}[/cyan]") for key in presets]
        self.show_panel(panel_lst)
    

    def choose_map(self, presets):
        choices = [{"name": key.capitalize() + " dungeon", "value": presets[key]} for key in presets]
        message = "\nChoose on which adventure your team will go:"
        choices.append({"name": "Compare maps", "value": self.map_preset_comparission})
        while True: #TODO while true is not good practice, in future change this to more good looking and safe 
            preset = make_query(message=message, choices=choices)
            if isinstance(preset, dict):
                return preset
            preset(presets)
        