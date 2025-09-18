from PlayerClasses.Inventory.item_generator import Item_generator

class Shop:
    def __init__(self, team):
        self.item_generator = Item_generator()
        self.team = team
        self.stock = []
        self.size_of_stock = 6

    def generate_stock(self):
        for i in range(self.size_of_stock):
            item = self.item_generator.generate_item(difficulty_key="shop", level=self.team.get_team_level())
            stock_dict = {"price": 0, "item": item} #TODO item price
            self.stock.append(stock_dict)

    def refresh_shop(self):
        self.stock = []
        self.generate_stock()
    
    def buy_item(self, idx): #TODO add payment
        item = self.stock[idx]["item"]
        self.stock.remove(item)
        self.team.stash.add_item(item)
    
    def get_shop_panels(self):
        panels = []
        for stock_dict in self.stock:
            panels.append(stock_dict["item"].get_item_panel())
        return panels