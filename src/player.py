# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move_player(self, user_input):
        next_room = getattr(self.current_room, f"{user_input}_to")
        if next_room == "invalid":
            print("==Area is out of bounds==")
        else: 
            self.current_room = next_room

    def drop_item(self, item):
        #is the item in the room?
        is_in_inventory = 0
        for x in range(len(self.inventory)):
            if self.inventory[x].name.lower() == item:
                self.current_room.items_list[self.inventory[x].name] = self.inventory[x]
                self.inventory[x].on_drop()
                self.inventory.pop(x)
                is_in_inventory = 1
        if is_in_inventory == 0:
            print(f"You never had {item} to begin with!")
    
    def take_item(self, item):
        is_in_room = 0
        #is the item in the room?
        for k, v in self.current_room.items_list.items():
            if v.name.lower() == item:
                self.inventory.append(v)
                v.on_take()
                is_in_room = 1
                key = k
        if is_in_room == 1:
            self.current_room.items_list.pop(key)
        else:
            print("That item isn't in this room!")
    
    def print_inventory(self):
        if len(self.inventory) > 0:
                print("==Inventory==")
                for x in self.inventory:
                    print(x.name)
        else:
            print("Your pockets are empty")