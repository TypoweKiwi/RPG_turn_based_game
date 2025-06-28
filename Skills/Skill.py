class Skill():
    def __init__(self, skill_dict):
        self.name = skill_dict["name"]
        self.func = skill_dict["func"]
        self.cost = skill_dict["cost"]
        self.desc = skill_dict["desc"]
        self.skill_type = skill_dict["skill_type"]