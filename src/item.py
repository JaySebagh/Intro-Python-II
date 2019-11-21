class Item:
    def __init__(self, type, name, description):
        self.type = type
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'Item Type: {self.type}, Item Name: {self.name}, Item Description: {self.description} |'