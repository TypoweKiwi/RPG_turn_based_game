class Stats:
    def __init__(self, basic_stat_dict):
        self.max_hp = basic_stat_dict.get("max_hp", 0)
        self.max_mp = basic_stat_dict.get("max_mp", 0)
        self.max_stamina = basic_stat_dict.get("max_stamina", 0)
        self.attack_damage = basic_stat_dict.get("attack_damage", 0)
        self.critical_chance = basic_stat_dict.get("critical_chance", 0)
        self.ability_power = basic_stat_dict.get("ability_power", 0)
        self.speed = basic_stat_dict.get("speed", 0)
        self.resistance = basic_stat_dict.get("resistance", {})

        self.health_points = 0
        self.mana_points = 0
        self.stamina = 0
    
    def get_current_stats_percintile(self):
        hp_percintile = self.health_points/self.max_hp
        mana_percintile = self.mana_points/self.max_mp
        stamina_percintile = self.stamina/self.max_stamina
        return hp_percintile, mana_percintile, stamina_percintile

    def __add__(self, other):
        return Stats({
            "max_hp": self.max_hp + other.max_hp, 
            "max_mp": self.max_mp + other.max_mp,
            "attack_damage": self.attack_damage + other.attack_damage,
            "critical_chance": self.critical_chance + other.critical_chance,
            "ability_power": self.ability_power + other.ability_power,
            "speed": self.speed + other.speed,
            "resistance": {key: self.resistance.get(key, 0) + other.resistance[key] for key in other.resistance} 
        })

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