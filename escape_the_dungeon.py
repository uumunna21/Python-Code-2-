import random

rooms = {
    'Hall': {
        'north': 'Kitchen',
        'east': 'Living Room',
        'west': 'Bathroom'
    },
    'Kitchen': {
        'south': 'Hall'
    },
    'Living Room': {
        'west': 'Hall',
        'north': 'Garden'
    },
    'Bathroom': {
        'east': 'Hall'
    },
    'Garden': {}
}

items = {
    'Hall': 'key',
    'Kitchen': 'map',
    'Living Room': '',
    'Bathroom': 'potion',
    'Garden': 'exit'
}

inventory = []

def show_instructions():
    print("Escape the Dungeon")
    print("Collect items and find the exit.")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get 'item name'")

def show_status(current_room):
    print("---------------------------")
    print(f"You are in the {current_room}")
    if items[current_room]:
        print(f"You see a {items[current_room]}")
    print("Inventory:", inventory)
    print("---------------------------")

def main():
    current_room = 'Hall'
    show_instructions()

    while True:
        show_status(current_room)
        move = input("> ").lower().split()

        if move[0] == 'go':
            direction = move[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")
        
        if move[0] == 'get':
            item = move[1]
            if items[current_room] == item:
                inventory.append(item)
                items[current_room] = ''
                print(f"{item} got!")
            else:
                print("Can't get that!")

        if 'exit' in inventory:
            print("Congratulations! You've escaped the dungeon!")
            break

if __name__ == "__main__":
    main()