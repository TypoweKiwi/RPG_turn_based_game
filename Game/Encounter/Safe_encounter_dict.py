from Game.Encounter.Safe_encounter_func import fountain_of_life_func, old_wizzard_func, mana_source_func, lost_adventurer_func, town_func

fountain_of_life = {
    "name": "Fountain of life",
    "desc": "You come across an ancient marble fountain, its waters glowing with a soft, golden light. As you approach, a warm energy washes over you — this is the legendary Fountain of Life.",
    "action": fountain_of_life_func
}

old_wizzard = {
    "name": "Old wizard",
    "desc": "An old wizard sits by the roadside, his eyes gleaming with ancient knowledge. He offers to teach you a forgotten skill... for free.",
    "action": old_wizzard_func
}

mana_source = {
    "name": "Mana source",
    "desc": "You find a bubbling spring of pure mana nestled among moss-covered stones. Its energy radiates into the air, calming and refreshing your mind.", 
    "action": mana_source_func
}

lost_adventurer = {
    "name": "Lost adventurer",
    "desc": "A weary adventurer stumbles out of the woods. He looks at you with tired eyes and asks, 'Mind if I join your party?'",
    "action": lost_adventurer_func
}

town = {
    "name": "Small Town",
    "desc": "You arrive at a small, peaceful town. The inn welcomes you with warmth, food, and soft beds — a perfect place to rest and recover.",
    "action": town_func
}

safe_encounter_places = [
    fountain_of_life,
    old_wizzard,
    mana_source,
    lost_adventurer,
    town,
]