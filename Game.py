import time

class Player:
    def __init__(self):
        self.inventory = []
        self.progress = 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print("Inventory:", ', '.join(self.inventory))

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mystical land full of challenges and wonders.")
    time.sleep(1)
    print("Your quest awaits...")

def make_choice(choices):
    print("\nChoose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_scene(player):
    print("\nYou enter a dark and mysterious forest.")
    time.sleep(1)
    print("As you walk deeper, you encounter a fork in the path.")
    time.sleep(1)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou chose the left path.")
        time.sleep(1)
        print("You discover a hidden treasure chest!")
        player.add_to_inventory("Golden Key")
        player.progress += 1
    else:
        print("\nYou chose the right path.")
        time.sleep(1)
        print("You encounter a hostile creature!")
        time.sleep(1)
        print("You manage to escape but get injured.")
        player.progress -= 1

def castle_scene(player):
    print("\nYou arrive at a grand castle.")
    time.sleep(1)
    print("The castle gate is locked.")
    time.sleep(1)

    if "Golden Key" in player.inventory:
        print("You use the Golden Key to unlock the gate.")
        player.progress += 1
    else:
        print("You need a key to unlock the gate. Explore more to find it.")

def conclusion(player):
    print("\nYour adventure comes to an end.")
    time.sleep(1)

    if player.progress >= 2:
        print("Congratulations! You successfully completed the quest and unlocked the castle gate.")
        time.sleep(1)
        print("You are hailed as a hero in the mystical land.")
    else:
        print("Your journey was challenging, but you did not complete the quest.")
        time.sleep(1)
        print("The castle gate remains locked.")

def main():
    player = Player()
    introduction()

    forest_scene(player)

    if player.progress >= 1:
        castle_scene(player)

    conclusion(player)

if __name__ == "__main__":
    main()
