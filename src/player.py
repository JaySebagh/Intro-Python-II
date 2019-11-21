# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, player, room):
        self.player = player
        self.room = room
        self.inventory = []
    
    def __repr__(self):
        return f'({repr(self.player)}, {repr(self.room)})'

    def move(self, command):
        moveList = ["n", "e", "s", "w"]
        try:
            moveList.index(command)
            if(command == "q"):
                return
            
            thisRoom = getattr(self.room, command + "_to")
            if(thisRoom):
                self.room = thisRoom
            else:
                print("No room found")
            self.room.onRoomChange()
        except:
            print("Failed")
            pass

    def playerInventory(self):
        return f'({self.player}\'s Inventory: {self.inventory})'

    def take_item(self, item):
        for i in range(len(self.room.items)):
            if self.room.items[i].type == item:
                removingItem = self.room.remove_item(item)
                self.inventory.append(removingItem)
                self.playerInventory()

    def drop_item(self, item):
        for element in self.inventory:
            if element.type == item:
                self.inventory.remove(element)
                self.room.add_item(element)