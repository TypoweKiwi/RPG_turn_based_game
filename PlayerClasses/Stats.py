#Base scaling values and patterns - for diffrent classes and items both can be changed
growth_factors = {
    "max_hp": 1.2,
    "max_mp": 1.15,
    "max_stamina": 1.1,
    "attack_damage": 1.1,
    "critical_chance": 1.005,
    "ability_power": 1.1,
    "speed": 1.01
}

scaling_pattern = {
    "max_hp": lambda base, level, f: int(base * (level ** f)),
    "max_mp": lambda base, level, f: int(base * (level ** f)),
    "max_stamina": lambda base, level, f: int(base * (level ** f)),
    "attack_damage": lambda base, level, f: int(base * (level ** f)),
    "critical_chance": lambda base, level, f: int(base * (level ** f)),
    "ability_power": lambda base, level, f: int(base * (level ** f)),
    "speed": lambda base, level, f: int(base * (level ** f))
}
    
class Stats:
    def __init__(self, basic_stat_dict, level=1, growth_factors=growth_factors, scaling_pattern=scaling_pattern): #TODO diffrent growthfactors for diffrent classes
        self.growth_factors = growth_factors
        self.scaling_pattern = scaling_pattern
        self.basic_stats_dict = basic_stat_dict
        self.update_stats(level)
        self.resistance = self.basic_stats_dict.get("resistance", {})
        self.health_points = self.max_hp
        self.mana_points = self.max_mp
        self.stamina = self.max_stamina
    
    def calculate_stat_value(self, key, level):
        return self.scaling_pattern[key](self.basic_stats_dict.get(key, 0), level, self.growth_factors[key])
    
    def update_stats(self, level):
        self.max_hp = self.calculate_stat_value("max_hp", level)
        self.max_mp = self.calculate_stat_value("max_mp", level)
        self.max_stamina = self.calculate_stat_value("max_stamina", level)
        self.attack_damage = self.calculate_stat_value("attack_damage", level)
        self.critical_chance = self.calculate_stat_value("critical_chance", level)
        self.ability_power = self.calculate_stat_value("ability_power", level)
        self.speed = self.calculate_stat_value("speed", level)

    def get_current_stats_percintile(self):
        hp_percintile = self.health_points/self.max_hp 
        mana_percintile = self.mana_points/self.max_mp if self.max_mp > 1 else 0
        stamina_percintile = self.stamina/self.max_stamina if self.max_stamina > 1 else 0
        return hp_percintile, mana_percintile, stamina_percintile

    def __add__(self, other):
        all_keys = set(self.resistance.keys()) | set(other.resistance.keys())
        return Stats({
            "max_hp": self.max_hp + other.max_hp, 
            "max_mp": self.max_mp + other.max_mp,
            "max_stamina": self.max_stamina + other.max_stamina,
            "attack_damage": self.attack_damage + other.attack_damage,
            "critical_chance": self.critical_chance + other.critical_chance,
            "ability_power": self.ability_power + other.ability_power,
            "speed": self.speed + other.speed,
            "resistance": {key: self.resistance.get(key, 0) + other.resistance.get(key, 0) for key in all_keys} 
        }, level=1)

    def get_stats_str(self):
        return (
            f"[red]HP[/red]: {self.health_points:.2f}/{self.max_hp}\n"
            f"[blue]MP[/blue]: {self.mana_points:.2f}/{self.max_mp}\n"
            f"[yellow]ST[/yellow]: {self.stamina:.2f}/{self.max_stamina}\n"
            f"[cyan]ATK[/cyan]: {self.attack_damage}\n"
            f"[magenta]AP[/magenta]: {self.ability_power}\n"
            f"[green]CRIT%[/green]: {self.critical_chance:.1f}%\n"
            f"[white]SPD[/white]: {self.speed}\n"
        )
    
    def get_item_stats_str(self): #Method that works only for items (Items will not show stats than have value 0)
        def format_stats(label, value): #Helper function to clear stats that item does not give
            if value == 0:
                return ""
            else:
                return f"{label}: {value:.2f}"
        stats_str_parts = [
            format_stats("[red]Max HP[/red]", self.max_hp),
            format_stats("[blue]Max MP[/blue]", self.max_mp),
            format_stats("[yellow]Max ST[/yellow]", self.max_stamina),
            format_stats("[cyan]ATK[/cyan]", self.attack_damage),
            format_stats("[magenta]AP[/magenta]", self.ability_power),
            format_stats("[green]CRIT%[/green]", self.critical_chance),
            format_stats("[white]SPD[/white]", self.speed)
        ]
        return "\n".join([part for part in stats_str_parts if part])
    
    def get_resistance_str(self):
        color_dict = {
            "physical": "red",
            "elemental": "blue",
            "holy": "bright_white",
            "dark": "magenta"
        }
        resistances = ""
        for type, val in self.resistance.items():
            color = color_dict[(type.lower())]
            resistances += f"\n[{color}]{type.upper()}[/]: {val}%"

        return f"{resistances}"
    
    def get_damage_multiplayers(self):
        dict = {
            "AD": self.attack_damage,
            "AP": self.ability_power,
            "HP": self.max_hp,
            "MP": self.max_mp,
            "SPD": self.speed,
            "Crit": self.critical_chance
        } 
        return dict