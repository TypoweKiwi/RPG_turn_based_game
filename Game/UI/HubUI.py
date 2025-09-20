from rich.console import Console
from Game.UI.Choices_func import make_query, show_message
from rich.columns import Columns
from rich.panel import Panel

class HubUI:
    def __init__(self, team):
        self.team = team
    
    def show_panel(self, panel):
        console = Console()
        with console.screen(style="on black"):
            console.print("\n" * 2)
            console.print(Columns(panel, expand=False, equal=False))
            show_message("")

    def map_preset_comparission(self):
        def get_preset_str(preset):
            return (
                f"[blue]Room numbers[/blue]: {preset['max_steps']}\n"
                f"[green]Safe room numbers[/green]: {preset['safe_zones_number']}\n"
                f"[red]Max enemies in room[/red]: {preset['max_enemies']}\n"
                f"[magenta]Boss[/magenta]: {preset['boss']}\n"
                f"[yellow]Gold cost[/yellow]: {preset['cost']}"
            )
        
        panel_lst = [Panel(get_preset_str(self.presets[key]), title=f"[cyan]{key.capitalize() + ' dungeon'}[/cyan]") for key in self.presets]
        self.show_panel(panel_lst)
    

    def choose_map(self, presets):
        self.presets = presets
        message = "\nChoose on which adventure your team will go:"
        choices = [{"name": key.capitalize() + " dungeon", "value": presets[key]} for key in presets]
        choices.append({"name": "Compare maps", "value": self.map_preset_comparission})
        choices.append({"name": f"Current team gold: {self.team.stash.wallet.gold_value}", "value": lambda: None})
        choices.append({"name": "Back", "value": self.exit_view_panel})
        self.view_status = True 
        while self.view_status:
            preset = make_query(message=message, choices=choices)
            if isinstance(preset, dict):
                if self.team.stash.wallet.try_payment(preset["cost"]):
                    return preset
            else:
                preset()
        return None

    def exit_view_panel(self):
        self.view_status = False
        
    def next_page(self, items=[]):
        if self.stop < len(items):
            self.start += self.n_items_to_view
            self.stop = min(self.stop + self.n_items_to_view, len(self.filtered_items))

    def previous_page(self):
        if self.start > 0:
            self.start -= self.n_items_to_view
            self.stop = self.start + self.n_items_to_view
    
    def view_items(self):
        items = self.team.stash.filtered_items
        message = "\nChoose item to inspect/equip: "
        self.n_items_to_view = 5
        self.view_status = True
        self.start = 0
        while self.view_status: #We dynamicly make choices lst bacause item list changes after equiping - we want list to update if item is taken or given
            self.stop = min(self.start + self.n_items_to_view, len(items))
            choices = [{"name": f"{i+1}. {items[i].get_name()}", "value": (self.item_options, items[i])} for i in range(self.start, self.stop)] 
            choices.append({"name": "Next page", "value": (self.next_page, items)})
            choices.append({"name": "Previous page", "value": (self.previous_page, None)})
            choices.append({"name": "Back", "value": (self.exit_view_panel, None)})
            choice = make_query(message=message, choices=choices)
            func, arg = choice
            func(arg) if arg else func()
    
    def show_item_panel(self, item):
        self.show_panel([item.get_item_panel()])

    def item_options(self, item):
        message = "\nWhat would you do with this item?"
        choices = [
            {"name": "Inspect item", "value": lambda: self.show_item_panel(item)},
            {"name": "Equip item", "value": lambda: self.team.equip_item(item)},
            {"name": "Sell item", "value": lambda: print("Not implemented yet")}, #TODO sell item
            {"name": "Back", "value": lambda: None}
        ]
        choice = make_query(message=message, choices=choices)
        choice()
    
    def modify_player_inventory(self):
        self.view_status = True
        message = "\n What action you wish to perform?"
        choices = [
            {"name": "Inspect inventory", "value": lambda: self.inspect_player_inventory(self.team.choose_player())},
            {"name": "Take off item", "value": lambda: self.team.take_item_off()},
            {"name": "Back", "value": self.exit_view_panel}
        ]
        while self.view_status:
            choice = make_query(message, choices)
            choice()
    
    def inspect_player_inventory(self, player):
        panel_lst = []
        for key in player.inventory.inventory_dict:
            item = player.inventory.inventory_dict[key] 
            item_str = f"[{item.rarity_color}]{item.get_name()}[/{item.rarity_color}]" +"\n" + item.get_item_stats_str() if item else "No item"
            panel_lst.append(Panel((item_str), title=key.capitalize()))
        self.show_panel(panel_lst)         



