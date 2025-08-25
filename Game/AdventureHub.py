from Game.UI.HubUI import HubUI
from Game.UI.Choices_func import make_query

class AdventureHub:
    def __init__(self, players, difficulty_factor=1):
        self.players = players
        self.difficulty_factor = difficulty_factor #Implement difficulty_factor to options in games class let player choose difficulty of game :)
        self.n_completed_adventures = 0
        self.exit_flag = False
        self.hub_ui = HubUI()
    
    def make_decision(self):
        self.exit_flag = False 
        choices = self.get_hub_options()
        choice = make_query(message="Choose hub action", choices=choices)
        choice()
    
    def choose_adventure(self):
        pass
    
    def start_adventure(self):
        map = self.choose_adventure()
        map.begin_adventure()

    def visit_wizard(self):
        pass

    def open_shop(self):
        pass

    def open_stash(self):
        pass

    def check_team_info(self):
        pass

    def team_recovery(self):
        pass

    def recruit_adventurer(self):
        pass

    def exit_hub(self):
        self.exit_flag = True

    def get_hub_options(self):
        choices = [
            {"name": "Start expedition", "value": self.start_adventure},
            {"name": "Visit wizard", "value": self.visit_wizard},
            {"name": "Visit shop", "value": self.open_shop},
            {"name": "Open stash", "value": self.open_stash},
            {"name": "Team recovery", "value": self.team_recovery},
            {"name": "Check team information", "value": self.check_team_info},
            {"name": "Recruit adventurer", "value": self.recruit_adventurer},
            {"name": "Exit to menu", "value": self.exit_hub}
        ]
        return choices