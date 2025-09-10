class Stash:
    def __init__(self):
        self.items_list = []
        self.wallet = 0 #TODO add wallet class 
    
    def add_item(self, item):
        self.items_list.append(item)
    
    def get_item(self, idx):
        item = self.items_list[idx]
        self.items_list.remove(item)
        return item