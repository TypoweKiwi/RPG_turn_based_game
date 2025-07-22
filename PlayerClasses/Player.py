from DamageCalculations.Reducing_damage import reduce_dmg
from Game.Choices_func import make_query
from PlayerClasses.Classes import classes
from Skills.Skill import Skill
from Skills.Skills_list import Skill_cost_type

class Player: 
    def __init__(self, name, basic_stat_dict, hostile = False):
        self.name = name
        self.max_hp = basic_stat_dict["max_hp"]
        self.health_points = basic_stat_dict["max_hp"]
        self.max_mp = basic_stat_dict["max_mp"]
        self.mana_points = basic_stat_dict["max_mp"]
        self.max_stamina = basic_stat_dict["max_stamina"]
        self.stamina = basic_stat_dict["max_stamina"]
        self.attack_damage = basic_stat_dict["attack_damage"]
        self.critical_chance = basic_stat_dict["crit_chance"]
        self.ability_power = basic_stat_dict["ability_power"]
        self.speed = basic_stat_dict["speed"]
        self.resistance = basic_stat_dict["resistance"]
        self.skills = []
        self.hostile = hostile

    def take_hit(self, damage, type):
        damage = reduce_dmg(damage, self.resistance[type])
        print(f"{self.name} received {round(damage, 2)} points of damage")
        self.health_points -= damage

    def get_damage_multiplayers(self):
        dict = {
            "AD": self.attack_damage,
            "AP": self.ability_power,
            "Crit": self.critical_chance
        }
        return dict
    
    def get_skill_resources(self):
        dict = {
            Skill_cost_type.HP: self.health_points,
            Skill_cost_type.MP: self.mana_points,
            Skill_cost_type.Stamina: self.stamina
        }
        return dict
    
    def check_skills(self):
        avalible_skills = []
        att_dict = self.get_skill_resources()
        for skill in self.skills:
            dict = {
                "name": str(skill),
                "description": skill.desc,
                "value": skill
            }
            if skill.cost > att_dict[skill.cost_type]:
                dict["name"] = dict["name"] + f"(Not enough {skill.cost_type.value})"
                dict["value"] = None
            avalible_skills.append(dict)
        return avalible_skills
    
    def apply_skill_cost(self, skill):
        if skill.cost_type == Skill_cost_type.HP:
            self.health_points -= skill.cost
        elif skill.cost_type == Skill_cost_type.MP:
            self.mana_points -= skill.cost
        elif skill.cost_type == Skill_cost_type.Stamina:
            self.stamina -= skill.cost
        
    def learn_skill(self, skill_dict):
        skill = make_query(message="Which skill you wish to replace?", choices=(self.skills[1:] + ["None"]))
        if skill == "None":
            print("You decided to not replace any skill.")
        else:
            skill_index = self.skills.index(skill)
            self.skills[skill_index] = Skill(skill_dict=skill_dict)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Team:
    def __init__(self, name="Team"):
        self.name = name
        self._players = []

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Only Player instances can be added to the team.")
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
    
    def __add__(self, other):
        if isinstance(other, Team):
            return self._players + other._playersew_team
        raise TypeError("Can only add another Team.")

    def remove_player(self, player_name):
        self._players = [p for p in self._players if p.name != player_name]

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