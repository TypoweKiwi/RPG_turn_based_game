from Game.Choices_func import make_query
from PlayerClasses.Classes import classes
from PlayerClasses.Player import Player

class Team:
    def __init__(self, name="Team"):
        self.name = name
        self._players = []

    def add_player(self, player):
        if len(self._players) < 4:
            self._players.append(player)
            return True
        else:
            choice = make_query(message=f"Your team is full. To accept a traveler into your party, you must tell one of your team members to leave. Do you wish to continue?", choices=["Yes", "No"])
            if choice == "Yes":
                member = make_query(message="Who do you wish do replace?", choices=self._players)
                member_index = self._players.index(member)
                print(f"You replaced {self._players[member_index].name} with {player}")
                self._players[member_index] = classes[player]()
                return True
        return False
    
    def get_team_members(self):
        return self._players
    
    def __add__(self, other):
        if isinstance(other, Team):
            return self._players + other._players
        raise TypeError("Can only add another Team.")

    def remove_player(self, player):
        self._players.remove(player)

    def __getitem__(self, index):
        return self._players[index]

    def __setitem__(self, index, value):
        if isinstance(value, Player):
            self._players[index] = value
        else:
            raise TypeError("Only Player instances can be assigned.")
    
    def __len__(self):
        return len(self._players)

    def __iter__(self):
        return iter(self._players)

    def __repr__(self):
        return f"Team(name={self.name}, players={self._players})"