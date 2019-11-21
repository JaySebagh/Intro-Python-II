# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    def onRoomChange(self):
        print(self.name)
        print(self.description)

    def __str__(self):
        return f"name: {self.name} \ndescription: {self.description}"
    
    def __repr__(self):
        return f'room({repr(self.name)}, {repr(self.description)})'

# my_room  = Room("Outside Cave Entrance", "North of you, the cave mount beckon")
# print(my_room)