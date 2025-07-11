from InquirerPy import inquirer

def make_query(message, choices):
    choice = inquirer.select(
            message=message,
            choices= choices,
        ).execute()
    return choice 

def choose_targets(enemies, n_targets):
    targets = []
    remaining_enemies = enemies[:]
    
    if n_targets > len(enemies):
        n_targets = len(enemies)

    for i in range(n_targets):
        target = make_query(f"Choose target {i+1}:", remaining_enemies)
        targets.append(target)
        remaining_enemies.remove(target)

    return targets