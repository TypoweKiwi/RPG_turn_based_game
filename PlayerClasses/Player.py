from DamageCalculations.Reducing_damage import reduce_dmg
from Game.Choices_func import make_query
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
    
    def gets_stats_str(self):
        return (
            f"[red]HP[/red]: {self.health_points:.2f}/{self.max_hp}\n"
            f"[blue]MP[/blue]: {self.mana_points:.2f}/{self.max_mp}\n"
            f"[yellow]ST[/yellow]: {self.stamina:.2f}/{self.max_stamina}\n"
            f"[cyan]ATK[/cyan]: {self.attack_damage}\n"
            f"[magenta]AP[/magenta]: {self.ability_power}\n"
            f"[green]CRIT%[/green]: {self.critical_chance:.1f}%\n"
            f"[white]SPD[/white]: {self.speed}\n"
        )

    def get_resistance_str(self):
        color_dict = {
            "physical": "red",
            "elemental": "blue",
            "holy": "bright_white",
            "dark": "magenta"
        }
        resistances = ""
        for type, val in self.resistance.items():
            color = color_dict[(type.value.lower())]
            resistances += f"\n[{color}]{type.value.upper()}[/]: {val}%"

        return f"{resistances}"
            
    def get_skills_panel(self): #TODO
        pass
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name