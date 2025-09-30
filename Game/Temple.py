from Game.UI.Choices_func import choose_options

class Temple:
    def __init__(self, team):
        self.team = team
        self.recover_cost = 100*(self.team.get_team_level()**1.2)
    
    def update_cost(self):
        self.recover_cost = 100*(self.team.get_team_level()**1.2)
    
    def heal(self, players): #TODO encapsulate healing and mana
        for player in players:
            player.stats.health_points = player.stats.max_hp

    def recover_mana(self, players):
        for player in players:
            player.stats.mana_points = player.stats.max_mp

    def heal_team(self):
        message = f"Who do you want to heal? - Mark with spacebar \n Cost: {self.recover_cost} per character"
        players = choose_options(message=message, choices=self.team.get_team_members())
        cost = self.recover_cost*len(players)
        if self.team.stash.wallet.try_payment(cost):
            self.heal(players)

    def recover_team_mana(self):
        message = f"Who do you want to recover mana? - Mark with spacebar \n Cost: {self.recover_cost} per character"
        players = choose_options(message=message, choices=self.team.get_team_members())
        cost = self.recover_cost*len(players)
        if self.team.stash.wallet.try_payment(cost):
            self.recover_mana(players)
    
    def __eq__(self, other):
        return isinstance(other, Temple) and self.__dict__ == other.__dict__
    
    def to_save_dict(self):
        return {"recover_cost": self.recover_cost}
    
    def load_save_dict(self, save_dict):
        self.recover_cost = save_dict["recover_cost"]