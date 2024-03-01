from room import Room
from character import Enemy
from character import Character

kitchen = Room("Kitchen")
ballroom = Room ("Ballroom")
dining_hall = Room ("Dining Hall")

kitchen.set_description("A small kitchen")
ballroom.set_description("A large ballroom")
dining_hall.set_description("A large hall with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west" )
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave. set_conversation ("Braaaaaaiiiiiiiinnnnnnnnssssssss")
dave. set_weakness("cheese")
dining_hall.set_character(dave)
current_room = kitchen

kitchen.link_room(dining_hall, "south")
dining_hall. link_room(kitchen, "north") 
dining_hall. link_room(ballroom, "west")
ballroom. link_room(dining_hall, "east")
current_room = kitchen
new_character = Character("Alice", "A friendly adventurer")
new_character.set_conversation("Hello there!")
ballroom.set_character(new_character)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

key = Item("Key", "A shiny golden key")

kitchen.set_item(key)

player_inventory = []
player_inventory.append(kitchen.get_item())




while True:
    print("\n")
    current_room.get_details()
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        if key in player_inventory:
            print("You use the key to open the locked door.")
            current_room = current_room.move(command)
        break
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one to talk to in this room.")
    elif command == "fight":
        if current_room.character is not None:
            combat_item = input("What item do you want to fight with? ")
            result = current_room.character.fight(combat_item)
            if not result:
                print("Game over! You lost the fight.")
                break
        else:
            print("There is no one to fight in this room.")
    else:
        print("Invalid command. Try again.")
    
        
        

