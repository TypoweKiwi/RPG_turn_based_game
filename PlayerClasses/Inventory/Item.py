from PlayerClasses.Stats import Stats

class Item:
    def __init__(self, item_stats_dict):
        self.name = item_stats_dict["name"]
        self.desc = item_stats_dict["desc"]
        self.stats = Stats(item_stats_dict)
        self.slot = item_stats_dict["slot"]