class Stash:
    def __init__(self):
        self.items_list = []
    
    def add_item(self, item):
        self.items_list.append(item)
    
    def get_item(self, idx):
        item = self.items_list[idx]
        self.items_list.remove(item)
        return item