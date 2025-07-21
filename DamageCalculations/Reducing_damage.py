def reduce_dmg(dmg, resist): #TODO Damage calculation improment
    resist = min(95, resist)
    return dmg * (1-resist/100)