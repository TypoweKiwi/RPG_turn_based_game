from Game.Encounter.Encounter_desc import generate_encounter_desc
from Game.Encounter.Safe_encounter_dict import safe_encounter_places
from Game.Choices_func import make_query, choose_targets, show_message
from PlayerClasses.Team import Team
from Skills.Skills_list import Skill_type
from Monster.Monsters import monsters
from collections import deque 
from rich.columns import Columns
from rich.console import Console
import time
import random 

class Encounter:
    def __init__(self,  players, hostile):
        self.description = generate_encounter_desc(hostile)
        self.players = players

    def begin_encounter(self):
        pass

    def decision(self):
        pass

    def check_status(self):
        pass
    
    def generate_desc(self):
        pass

class HostileEncounter(Encounter): 
    def __init__(self, players, max_enemies):
        super().__init__(players, hostile=True)
        self.max_enemies = max_enemies
        self.enemies = Team(name="Enemies")
        self.order_queue = deque()
        for i in range(random.randint(1, self.max_enemies)):
            monster_key = random.choice(list(monsters.keys()))
            self.enemies.add_player(monsters[monster_key]())
        
        self.description += f"\nYour team encounter {self.enemies.get_team_members()}" #TODO better encounter status message

    def begin_encounter(self):  
        show_message(self.description)
        flag = 0
        i = 1
        while flag==0:
            self.calculate_turn_order()
            print(f"\nRound {i}\nCurrent turn order {[(i+1, self.order_queue[i]) for i in range(len(self.order_queue))]}") #TODO better turn message
            while self.order_queue:
                time.sleep(1)
                self.execute_turn()
                if self.check_combat_status():
                    flag = 1
                    break
            i += 1

    def calculate_turn_order(self):
        self.order_queue.clear()
        objects_sorted = self.players + self.enemies
        objects_sorted.sort(key=lambda x: x.speed)
        for obj in objects_sorted:
            self.order_queue.append(obj)
        self.order_queue.reverse()

    def execute_turn(self):
        obj = self.order_queue.popleft()
        print(f"\n{obj.name} turn")
        if obj.hostile:
            self.hostile_decision(obj) 
        else:
            self.player_decision(obj)

    def player_decision(self, player):
        choices=[
            {"name": f"Attack ({player.name} turn)", "value": self.player_attack},
            {"name": "Show Stats", "value": self.show_stats},
            {"name": "Show skills", "value": self.show_skills} #TODO self.show_skills
        ]
        decision = make_query(message="\nChoose your action", choices=choices)
        decision(player)
    
    def show_stats(self, player):
        resistance = make_query(message="\nWhich stats you wish to see?", choices=[{"name": "Vital Stats", "value": False}, {"name": "Resistance", "value": True}])
        console = Console()
        with console.screen(style="on black"):
            player_panels = self.players.player_stats_panel(resistance=resistance)
            enemy_panels = self.enemies.player_stats_panel(resistance=resistance)
            all_panels = player_panels + enemy_panels
            console.print(Columns(all_panels, expand=False, equal=False))
            show_message("")
        self.player_decision(player)
    
    def show_skills(self, player):
        pass
    
    def player_attack(self, player):
        skills = player.check_skills()
        ability = make_query("Choose ability", skills)
        while ability == None:
            print(f"You do not have enough {ability.cost_type.value } for this skill!")
            ability = make_query("Choose ability", skills)

        damage_multiplayers = player.get_damage_multiplayers()
        
        if ability.skill_type == Skill_type.SINGLE_TARGET: 
            target = make_query("Which enemy you wish to attack?", self.enemies) 
            ability.func(damage_multiplayers, target)
        elif ability.skill_type == Skill_type.AOE: 
            target = choose_targets(self.enemies, ability.n_targets) 
            ability.func(damage_multiplayers, target)
        elif ability.skill_type == Skill_type.SELF_CAST:
            target = player
            ability.func(damage_multiplayers, target)
        elif ability.skill_type == Skill_type.TEAM_CAST:
            target = make_query("On which team member you wish to cast ability?", self.players)
            ability.func(damage_multiplayers, target)

        player.apply_skill_cost(ability)
        self.check_targets_status(target)


    def hostile_decision(self, monster): #TODO More advance monster attack - maybe based on simple ML model
        target = random.choice(self.players)
        ability = random.choice(monster.check_skills())
        ability = ability["value"]
        damage_multiplayers = monster.get_damage_multiplayers()

        print(f"{monster.name} attacked {target.name} with {ability.name}!")
        ability.func(damage_multiplayers, target)
        self.check_targets_status(target)

    def check_targets_status(self, targets):
        if isinstance(targets, list):
            for target in targets:
               self.check_target_status(target)
        else:
            target = targets
            self.check_target_status(target)
            
    def check_target_status(self, target):  
        if target.health_points <= 0:
            print(f"{target.name} died")
            self.enemies.remove_player(target) if target.hostile else self.players.remove_player(target)
            
    def check_combat_status(self):   
        if not self.players:
            print("\nYou lost because your team died")
            return True
        elif not self.enemies:
            print("\nYou won by defeating all opponents")
            return True
        else:
            return False
        

class SafeEncounter(Encounter): #TODO safe encouner
    def __init__(self, players):
        super().__init__(players, hostile=False)
        self.encounter_dict = random.choice(safe_encounter_places)
        self.description += self.encounter_dict["desc"] 

    def begin_encounter(self):
        show_message(self.description)
        self.encounter_dict["action"](self.players)