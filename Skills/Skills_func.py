from DamageCalculations.Type import DamageType

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
          