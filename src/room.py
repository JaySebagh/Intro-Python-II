# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    
    def onRoomChange(self):
        print("Room Name: ", self.name)
        print("Room Description: ", self.description)
        print("Room Items", self.items)

    def __str__(self):
        return f"Room Name: {self.name} \nDescription: {self.description} \nItems: {self.items}"
    
    def __repr__(self):
        return f'room({repr(self.name)}, {repr(self.description)})'
    
    def add_item(self, item):
        self.items.append(item)
        
    
    def remove_item(self, item):
        for element in self.items:
            if element.type == item:
                self.items.remove(element)
                return element

    def room_items(self, items):
        return self.items