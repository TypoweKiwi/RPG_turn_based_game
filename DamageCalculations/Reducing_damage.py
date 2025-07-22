def reduce_dmg(dmg, resist): 
    resist = min(95, resist)
    return dmg * (1-resist/100)