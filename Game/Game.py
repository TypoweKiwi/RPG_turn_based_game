from PlayerClasses.Classes import classes
from InquirerPy import inquirer

class Game:
    def __init__(self):
        self.player = None
        self.map = None 
    
    def create_new_game(self):
        choice = inquirer.select(
            message="Chose your class:",
            choices= [element for element in classes],
        ).execute()
        print(f"Your class choice: {choice}")

        name = input("Write your name")
        self.player = classes[choice](name)