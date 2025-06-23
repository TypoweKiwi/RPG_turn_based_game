from enum import Enum

class DamageType(Enum):
    physical = 1
    magical = 2

class Fighter:
    def __init__(self, hp, ad, ap, name):
        self.name = name
        self.max_hp = hp
        self.health_points = hp
        self.attack_damage = ad
        self.ability_power = ap
        self.armor = 5
        self.magic_resist = 6

    def hit(self, target):
        physical_damage = 1
        magical_damage = 2
        target.take_hit(physical_damage, magical_damage)
    
    def take_hit(self, damage, type):
        if type == DamageType.physical:
            damage = reduce_dmg(damage, self.armor)
        elif type == DamageType.magical:
            damage = reduce_dmg(damage, self.magic_resist)
            
        self.health_points -= damage
    
    def __str__(self):
        return f"Player {self.name} Hp: {self.health_points}/{self.max_hp}"

def reduce_dmg(dmg, resist):
    return dmg - resist

f1 = Fighter(30, 10, 1)
f2 = Fighter(20, 10, 2)

while f1.health_points > 0 and f2.health_points > 0:
    f1.hit(f2)
    f2.hit(f1)
    print(f1)
    print(f2)