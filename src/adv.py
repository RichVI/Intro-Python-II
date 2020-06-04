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

def move_player(player_input):
    next_room = getattr(richard.current_room, f"{player_input}_to")
    if next_room == "invalid":
        print("==Area is out of bounds==")
    else: 
        richard.current_room = next_room
    game_loop()


# Make a new player object that is currently in the 'outside' room.
richard = Player("Richard", room["outside"])
print(f"\nPlayer Name: {richard.name}, welcome to the game! \n")
# Write a loop that:
#
def game_loop():
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    print(f"Location: {richard.current_room.name}\n{richard.current_room.description}\n\nWhere do you go next? [n] [e] [s] [w] [q] for quit]")
    player_input = input()
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    if player_input == "q":
        print("==Game Over==")
    elif player_input == "n" or player_input == "e" or player_input == "s" or player_input == "w":
        move_player(player_input)
    else:
        print("Please enter a valid direction, or q to quit the game!")

# If the user enters "q", quit the game.

game_loop()