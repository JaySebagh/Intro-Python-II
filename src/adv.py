from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playerName = input("Player Name: ")

currRoom = room['outside']
print(currRoom)


currPlayer = Player(playerName, currRoom)

while True:
    command = input("Cardinal Direction (n/e/s/w): ")
    currPlayer.move(command)










# userInput = ""
# def startQuest():
#     global userInput
#     global currRoom

#     userInput = input("Cardinal Direction (n/e/s/w): ")

#     if currRoom.name == "Outside Cave Entrance":
#         if userInput == "n":
#             # currRoom = Room(room['foyer'].name, room['foyer'].description)
#             currPlayer = Player(playerName, room['foyer'])
#             print(f'{currPlayer.player}\'s current position: \n{currRoom}')
#             startQuest()
#         elif userInput == "e" or userInput == "s" or userInput == "w":
#             print("Movement is not allowed")
#             startQuest()
#     elif currRoom.name == "Foyer":
#         if userInput == "s":
#             # currRoom = Room(room['outside'].name, room['outside'].description)
#             currPlayer = Player(playerName, room['outside'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "n":
#             # currRoom = Room(room['overlook'].name, room['overlook'].description)
#             currPlayer = Player(playerName, room['overlook'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "e":
#             # currRoom = Room(room['narrow'].name, room['narrow'].description)
#             currPlayer = Player(playerName, room['narrow'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "w":
#             print("Movement is not allowed")
#             startQuest()
#     elif currRoom.name == "Grand Overlook":
#         if userInput == "s":
#             # currRoom = Room(room['foyer'].name, room['foyer'].description)
#             currPlayer = Player(playerName, room['foyer'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "e" or userInput == "n" or userInput == "w":
#             print("Movement is not allowed")
#             startQuest()
#     elif currRoom.name == "Narrow Passage":
#         if userInput == "w":
#             # currRoom = Room(room['foyer'].name, room['foyer'].description)
#             currPlayer = Player(playerName, room['foyer'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "n":
#             # currRoom = Room(room['treasure'].name, room['treasure'].description)
#             currPlayer = Player(playerName, room['treasure'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "e" or userInput == "s":
#             print("Movement is not allowed")
#             startQuest()
#     elif currRoom.name == "Treasure Chamber":
#         if userInput == "s":
#             # currRoom = Room(room['narrow'].name, room['narrow'].description)
#             currPlayer = Player(playerName, room['narrow'])
#             print(currRoom)
#             startQuest()
#         elif userInput == "e" or userInput == "n" or userInput == "w":
#             print("Movement is not allowed")
#             startQuest()
#     elif userInput == "q":
#         quit()

# startQuest()