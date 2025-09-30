from Game.UI.Choices_func import show_message

class Wallet:
    def __init__(self):
        self.gold_value = 0
    
    def pay(self, amount):
        self.gold_value -= amount
    
    def earn(self, amount):
        self.gold_value += amount
    
    def try_payment(self, value):
        if self.gold_value >= value:
            self.pay(value)
            show_message(f"You have successfully made this transaction.\nCurrent gold after transaction: {self.gold_value}")
            return True
        else:
            show_message(f"You do not have enough gold to make this transaction.\nCurrent gold: {self.gold_value}\nPayment cost: {value}")
            return False
    
    def __eq__(self, other):
        return isinstance(other, Wallet) and self.__dict__ == other.__dict__

    def to_save_dict(self):
        return self.__dict__
    
    def load_save_dict(self, save_dict):
        self.__dict__ = save_dict