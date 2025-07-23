class Skill():
    def __init__(self, skill_dict):
        self.name = skill_dict["name"]
        self.func = skill_dict["func"]
        self.cost = skill_dict["cost"]
        self.cost_type = skill_dict["cost_type"]
        self.desc = skill_dict["desc"]
        self.skill_type = skill_dict["skill_type"]
        self.n_targets = skill_dict["n_targets"]

    def __str__(self):
        return f"{self.name} | {self.skill_type.name} | {self.cost} {self.cost_type.value}"