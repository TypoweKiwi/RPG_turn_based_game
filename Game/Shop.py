from PlayerClasses.Inventory.item_generator import Item_generator
from Game.UI.Choices_func import show_message

class Shop:
    def __init__(self, team):
        self.item_generator = Item_generator()
        self.team = team
        self.stock = []
        self.size_of_stock = 6

    def generate_stock(self):
        for i in range(self.size_of_stock):
            item = self.item_generator.generate_item(difficulty_key="shop", level=self.team.get_team_level())
            item.price = int(item.price*1.2) #We add 20% to the item price to make it more expensive
            self.stock.append(item)

    def refresh_shop(self):
        refresh_price = 500*(self.team.get_team_level()**1.2)
        if self.team.stash.wallet.try_payment(refresh_price):
            self.stock = []
            self.generate_stock()
    
    def buy_item(self, idx): 
        item = self.stock[idx]
        if self.team.stash.wallet.try_payment(item.price):
            self.stock.remove(item)
            item.price = item.base_price
            self.team.stash.add_item(item)
    
    def get_shop_panels(self):
        panels = []
        for item in self.stock:
            panels.append(item.get_item_panel())
        return panels
    
    def upgrade_item(self, item):
        if item.upgrade_counter >= item.max_upgrade_level:
            show_message("Item is already at max upgrade level")
            return None
        upgraded_item_price = item.calculate_price(item.level + 1)
        upgrade_cost = upgraded_item_price*0.5
        if self.team.stash.wallet.try_payment(upgrade_cost):
            item.upgrade()
        