from PlayerClasses.Player import Player, DamageType

class Cleric(Player):
    def ability_1(self, target): #holy smite
        skill_damage = 5
        damage = skill_damage*self.ability_power
        target.take_hit(damage, DamageType.holy)

    def ability_2(self): #heal
        self.health_points + 20

    def ability_3(self, *targets): #Prayer
        skill_damage = 3
        damage = skill_damage*self.ability_power
        for target in targets:
            target.take_hit(damage, DamageType.holy)
    
    def get_abilities(self):
        abilities_lst = [
            ("Holy smite", self.ability_1)
            ("Heal", self.ability_2)
            ("Prayer", self.ability_3)
        ]