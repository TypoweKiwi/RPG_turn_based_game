from Game.UI.Choices_func import make_query, choose_targets, show_message
from Game.UI.UI import UI
from Skills.Skills_list import Skill_type
from rich.columns import Columns
from rich.console import Console

class CombatUI(UI):
    def __init__(self, team, enemies):
        super().__init__(team, enemies)

    def player_decision(self, player):
        choices=[
            {"name": f"Attack ({player.name} turn)", "value": self.player_attack},
            {"name": "Show Stats", "value": self.show_vital_stats},
            {"name": "Show Resistances", "value": self.show_resistances},
            {"name": "Show skills", "value": self.show_skills} 
        ]
        result = None
        while result is None:
            decision = make_query(message="\nChoose your action", choices=choices)
            result = decision(player)
        return result
    
    def player_attack(self, player):
        skills = player.check_skills()
        skills.append({"name": "Back", "value": "BACK"})

        while True:
            ability = make_query("Choose ability", skills)
            if ability == "BACK":
                return self.player_decision(player)
            elif ability is None:
                print(f"You do not have enough resources to use this skill!")
                continue
            break
        
        if ability.skill_type == Skill_type.SINGLE_TARGET: 
            target = make_query("Which enemy you wish to attack?", self.enemies) 
        elif ability.skill_type == Skill_type.AOE: 
            target = choose_targets(self.enemies, ability.n_targets) 
        elif ability.skill_type == Skill_type.SELF_CAST:
            target = player
        elif ability.skill_type == Skill_type.TEAM_CAST:
            target = make_query("On which team member you wish to cast ability?", self.team)
        
        return ability, target