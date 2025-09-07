from DamageCalculations.Reducing_damage import reduce_dmg
from Game.UI.Choices_func import make_query
from Skills.Skill import Skill
from Skills.Skills_list import Skill_cost_type
from PlayerClasses.Inventory.Inventory import Inventory
from PlayerClasses.Stats import Stats
from rich.panel import Panel

class Player: 
    def __init__(self, name, basic_stat_dict, hostile = False, level=1):
        self.name = name
        self.hostile = hostile

        #Stats - We hold two variables: one for player stats and other for sum of player and invetory stats
        self.base_stats = Stats(basic_stat_dict, level)
        self.stats = self.base_stats 

        #Skills/inventory/Level/Exp
        self.skills = []
        self.inventory = Inventory()
        self.set_level(level)
        self.current_exp = 0
    
    def set_level(self, level):
        self.level = level
        self.required_exp = int(100*(self.level)**2)
        self.base_stats.update_stats(self.level)
        self.recalculate_stats()
    
    def check_level_up(self):
        while self.current_exp >= self.required_exp:
            self.current_exp -= self.required_exp
            self.set_level(level=self.level+1) #TODO announcement about level up 
    
    def gain_exp(self, amount):
        self.current_exp += amount
        self.check_level_up()

    def take_hit(self, damage, type):
        damage = reduce_dmg(damage, self.stats.resistance[type.name])
        print(f"{self.name} received {round(damage, 2)} points of damage")
        self.stats.health_points -= damage
    
    def recalculate_stats(self):
        hp_perc, mana_perc, stamina_perc = self.stats.get_current_stats_percintile() #Dynamic statistics are calculated as a percentage
        self.stats = self.base_stats + self.inventory.get_inventory_stats() #Add method do not add dynamic stats like hp and mp
        self.stats.health_points = self.stats.max_hp * hp_perc
        self.stats.mana_points = self.stats.max_mp * mana_perc
        self.stats.stamina = self.stats.max_stamina * stamina_perc
    
    def get_skill_resources(self):
        dict = {
            Skill_cost_type.HP: self.stats.health_points,
            Skill_cost_type.MP: self.stats.mana_points,
            Skill_cost_type.Stamina: self.stats.stamina
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
            self.stats.health_points -= skill.cost
        elif skill.cost_type == Skill_cost_type.MP:
            self.stats.mana_points -= skill.cost
        elif skill.cost_type == Skill_cost_type.Stamina:
            self.stats.stamina -= skill.cost
        
    def learn_skill(self, skill_dict):
        skill = make_query(message="Which skill you wish to replace?", choices=(self.skills[1:] + ["None"]))
        if skill == "None":
            print("You decided to not replace any skill.")
        else:
            skill_index = self.skills.index(skill)
            self.skills[skill_index] = Skill(skill_dict=skill_dict)
    
    def gets_stats_str(self):
        return self.stats.get_stats_str()

    def get_resistance_str(self):
        return self.stats.get_resistance_str()
    
    def get_damage_multiplayers(self):
        return self.stats.get_damage_multiplayers()
    
    def update_from_dict(self, stats):
        for key, value in stats.items():
            if hasattr(self, key):
                setattr(self, key, value)
            
    def get_skills_panel(self): 
        return [Panel(skill.get_skill_str(), title=f"[magenta]{skill.name}[/magenta]") for skill in self.skills]
    
    def __eq__(self, other):
        return isinstance(other, Player) and self.__dict__ == other.__dict__
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name