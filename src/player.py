# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player, room):
        self.player = player
        self.room = room
    
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

        # print(self.room.n_to.name)
        # self.room = self.room[command + "_to"]





        # if command in moveList:
        #     command