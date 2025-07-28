class Skill():
    def __init__(self, skill_dict):
        self.name = skill_dict["name"]
        self.func = skill_dict["func"]
        self.cost = skill_dict["cost"]
        self.cost_type = skill_dict["cost_type"]
        self.desc = skill_dict["desc"]
        self.skill_type = skill_dict["skill_type"]
        self.n_targets = skill_dict["n_targets"]
        self.damage_type = skill_dict["dmg_type"]
        self.scaling = skill_dict["scaling"]
        self.effect = skill_dict["effect"]
        self.crit = skill_dict.get("crit", False)
        
    def use_skill(self, stats_dict, target):
        skill_dict = {
            "dmg_type": self.damage_type,
            "scalling": self.scaling,
            "crit": self.crit
        }
        self.func(stats_dict, target, skill_dict)

    def get_skill_str(self):
        cost_colors = {
            "MP": "blue",
            "Stamina": "yellow",
            "HP": "red"
        }

        dmg_colors = {
            "physical": "red",
            "elemental": "blue",
            "holy": "bright_white",
            "dark": "magenta"
        }

        cost_color = cost_colors[self.cost_type.value]
        dmg_color = dmg_colors[self.damage_type.name]
        scaling_str = f"{self.scaling['base']} × ({self.scaling['type']} x {self.scaling.get('factor', 1)})"
        targets_str = f"{self.n_targets} target{'s' if self.n_targets > 1 else ''}"
        return (
            f"[italic]{self.desc}[/italic]\n\n"
            f"[cyan]Cost:[/] [{cost_color}]{self.cost} {self.cost_type.value}[/]\n"
            f"[cyan]Effect:[/] {self.effect}\n"
            f"[cyan]Scaling:[/] {scaling_str}\n"
            f"[cyan]Damage Type:[/] [{dmg_color}]{self.damage_type.name.upper()}[/]\n"
            f"[cyan]Skill Type:[/] {self.skill_type.value} ({targets_str})\n"
            f"[cyan]Crit:[/] {'[green]Yes[/]' if self.crit else '[red]No[/]'}"
        )

    def __str__(self):
        return f"{self.name} | {self.skill_type.name} | {self.cost} {self.cost_type.value}"