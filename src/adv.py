from room import Room
from player import Player
from item import Item
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

items = {
    "bow": Item("bow", "Dwarven Black Bow of Fate", "DMG: 13, Weight: 10, Value: 1446"),
    "axe": Item("axe", "Drainblood Battleaxe", "DMG: 21, Weight: 5, Value: 266"),
    "sword": Item("sword", "Ebony Blade", "DMG: 11, Weight: 10, Value: 2000"),
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

room['foyer'].add_item(items["sword"])
room['narrow'].add_item(items["axe"])
room['treasure'].add_item(items["bow"])

# Main
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
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

    splitCommand = command.split()

    if len(command) == 1:
        currPlayer.move(command)
    elif len(splitCommand) == 2:
        if splitCommand[0] == "take":
            currPlayer.take_item(splitCommand[1])
        elif splitCommand[0] == "drop":
            currPlayer.drop_item(splitCommand[1])