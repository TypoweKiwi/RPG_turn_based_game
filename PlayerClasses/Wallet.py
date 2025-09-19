from Game.UI.Choices_func import show_message

class Wallet:
    def __init__(self):
        self.gold_value = 0
    
    def pay(self, amount):
        self.gold_value -= amount
    
    def earn(self, amount):
        self.gold_value += amount
    
    def try_payment(self, value=None):
        if self.gold_value >= value:
            self.pay(value)
            return True
        else:
            show_message(f"You do not have enough gold to make this transaction.\nCurrent gold: {self.gold_value}\nPayment cost: {value}")
            return False