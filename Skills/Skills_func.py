from DamageCalculations.Type import DamageType
import random

def basic_attack_func(target, attack_damage, crit_chance):
    ticket = random.random(0.01, 1)
    damage = attack_damage*2 if crit_chance >= ticket else attack_damage
    target.take_hit(damage, DamageType.physical)

def holy_smite_func(target, ability_power):
    skill_damage = 5
    damage = skill_damage*ability_power
    target.take_hit(damage, DamageType.holy)

def heal_func(target):
    heal_amount = 10
    target.health_points = min(target.max_hp, target.health_points + heal_amount)

def prayer_func(*targets, ability_power):
    skill_damage = 3
    damage = skill_damage*ability_power
    for target in targets:
        target.take_hit(damage, DamageType.holy)
          
    