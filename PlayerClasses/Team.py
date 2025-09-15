from PlayerClasses.Classes import classes
from PlayerClasses.Player import Player, Panel, make_query
from PlayerClasses.Inventory.Stash import Stash

class Team:
    def __init__(self, name="Team"):
        self.name = name
        self._players = []
        self.stash = Stash()

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

    def remove_player(self, player):
        self._players.remove(player)
    
    def get_team_members(self):
        return self._players
    
    def player_stats_panel(self, resistance=False):
        panel_lst = []
        for player in self._players:
            color = "red" if player.hostile else "green"
            stats_str = player.get_resistance_str() if resistance else player.gets_stats_str()
            panel_lst.append(Panel(stats_str, title=f"[{color}]{player.name}[/{color}]"))
        return panel_lst
    
    def add_gold(self, amount):
        self.wallet += amount
    
    def remove_gold(self, amount):
        self.wallet -= amount
    
    def get_team_level(self):
        sum_level = 0
        for player in self._players:
            sum_level += player.level
        return int(sum_level/len(self._players))

    def choose_player(self):
        message = "On which character you wish to perform action?"
        return make_query(message=message, choices=self._players.copy())
    
    def equip_item(self, item):
        player = self.choose_player()
        player.inventory.equip_item(item, self.stash)
        self.stash.items_list.remove(item)
    
    def take_item_off(self):
        player = self.choose_player()
        message = "From which slot do you wish to unequip item?"
        choices = [{"name": key.capitalize(), "value": key} for key in player.inventory.inventory_dict]
        slot = make_query(message, choices)
        player.inventory.take_item_off(slot, self.stash)

    def __add__(self, other):
        if isinstance(other, Team):
            return self._players + other._players
        raise TypeError("Can only add another Team.")

    def __setitem__(self, index, value):
        if isinstance(value, Player):
            self._players[index] = value
        else:
            raise TypeError("Only Player instances can be assigned.")

    def __getitem__(self, index):
        return self._players[index]
    
    def __eq__(self, other):
        return isinstance(other, Team) and self.__dict__ == other.__dict__

    def __len__(self):
        return len(self._players)

    def __iter__(self):
        return iter(self._players)

    def __repr__(self):
        return f"Team(name={self.name}, players={self._players})"