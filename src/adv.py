from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


# Add items to the rooms
room["outside"].items_list = {
    "rice": Item("rice", "+20 Power")
}

room["foyer"].items_list = {
    "steak": Item("steak", "+30 Power"),
    "egg": Item("egg", "+40 Power")
}

room["overlook"].items_list = {
    "spicySteak": Item("spicySteak", "+50 Power")
}

room["narrow"].items_list = {
    "sandwich": Item("sandwich", "+60 Power")
}

room["treasure"].items_list = {
    "jerky": Item("jerky", "+70 Power")
}


#
# Main
#

# Make a new player object that is currently in the "outside" room.
richard = Player("richard", room["outside"]) 

# When a bad command is entered            
def valid_command_needed():
    print("Please enter a valid command, or q to quit the game!")
    game_loop()

#core loop of the game
def game_loop():
    
    #print location information
    print(f"\n==Location==\n{richard.current_room.name}\n{richard.current_room.description}\n")
    
    #print items information
    print("==Items==")
    if len(richard.current_room.items_list) == 0:
        print("There are no items in this room!")
    else:
        for k, v in richard.current_room.items_list.items():
            print(f"{v.name}: {v.description}")
    print("\n")

    #print player instructions
    print("Movement: [n] [e] [s] [w] [q for quit]\nPick up item: [Take [item]]\nDrop an item: [Drop [item]]\nInventory: [i]")
    
    #get input and act
    user_input = input().lower().split()
    
    if len(user_input) == 1:
        user_input = user_input[0]
        #if the user wants to quit
        if user_input.lower() == "q":
            print("==Game Over==")
        #if the user wants to see their inventory
        elif user_input == "i":
            richard.print_inventory()
            game_loop()
        #if the user wants to move around
        elif user_input == "n" or user_input == "e" or user_input == "s" or user_input == "w":
            richard.move_player(user_input)
            game_loop()
        else: 
            valid_command_needed()

    #two words! so they either want to drop something or pick it up
    elif len(user_input) == 2:
        #if the user wants to pick something up
        if user_input[0] == "take" or user_input[0] == "get":
            richard.take_item(user_input[1])
            game_loop()
        if user_input[0] == "drop":
            richard.drop_item(user_input[1])
            game_loop()
        else:
            valid_command_needed()
    else:
        valid_command_needed()

game_loop()