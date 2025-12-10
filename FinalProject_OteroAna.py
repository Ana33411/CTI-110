# Ana Otero
# Date
# Final Project
# T-Rex Escape Adventure Game
# A full text-based adventure game with branching paths, sound effects,
# random events, inventory, loops, and multiple functions.

import random

# ===============================
# INTRO
# ===============================
def intro():
    print("\n===================================================")
    print("              🦖 T-REX ESCAPE ADVENTURE 🦖")
    print("===================================================")
    print("You are touring Jurassic Canyon when the security power fails.")
    print("A giant T-Rex has escaped!")
    print("Survive by making smart choices.\n")


# ===============================
# INVENTORY SYSTEM
# ===============================
def find_item(inventory):
    """Random chance to find a useful item."""
    items = ["flashlight", "flare", "first-aid kit", "park map", None]

    found = random.choice(items)
    if found:
        print(f"\n✨ You found a **{found}** and added it to your inventory!")
        inventory.append(found)
    else:
        print("\nYou found nothing useful this time.")

    return inventory


# ===============================
# MAIN PATH SELECTION
# ===============================
def choose_path():
    print("\nYou see three escape options:")
    print("1. Run into the jungle")
    print("2. Hide inside an abandoned Jeep")
    print("3. Sneak into the maintenance tunnels")

    choice = input("Choose 1, 2, or 3: ")

    while choice not in ("1", "2", "3"):
        choice = input("Invalid — choose 1, 2, or 3: ")

    return choice


# ===============================
# JUNGLE PATH
# ===============================
def jungle_path(inventory):
    print("\n🌴 You sprint into the jungle!")
    print("Branches snap behind you — the T-Rex is following!")
    print("SFX: *THUD* ... *THUD* ... *ROOOOAR*")

    inventory = find_item(inventory)
    event = random.randint(1, 4)

    # SAFE RESULT 1
    if event == 1:
        print("\nYou climb a sturdy tree and stay perfectly still.")
        print("The T-Rex sniffs around but eventually walks away.")
        return True, inventory

    # SAFE RESULT 2
    if event == 2:
        print("\nYou dive into a river and let the current carry you away.")
        print("The T-Rex loses sight of you. You're safe!")
        return True, inventory

    # SAFE RESULT 3 (inventory bonus)
    if event == 3 and "flare" in inventory:
        print("\nYou use your flare to distract the T-Rex!")
        print("It chases the light while you escape. Smart thinking!")
        return True, inventory

    # BAD RESULT
    print("\nYou enter a clearing and come face-to-face with the T-Rex.")
    print("SFX: *ROOOAAAR!!*")
    return False, inventory


# ===============================
# JEEP PATH
# ===============================
def jeep_path(inventory):
    print("\n🚙 You slide into the abandoned Jeep...")
    print("SFX: *creak...* *click*")

    inventory = find_item(inventory)
    event = random.randint(1, 3)

    # SAFE
    if event == 1:
        print("\nThe T-Rex walks right past. It doesn't see you!")
        return True, inventory

    # SAFE 2
    if event == 2:
        print("\nKeys! You turn the ignition.")
        print("SFX: *VROOOOOOM!*")
        print("You speed away safely!")
        return True, inventory

    # CONDITIONAL SAFE
    if event == 3 and "park map" in inventory:
        print("\nThe T-Rex slams the Jeep, but you use the park map")
        print("to navigate a hidden back trail and escape!")
        return True, inventory

    # BAD RESULT
    print("\nThe T-Rex smashes the Jeep. You cannot escape.")
    return False, inventory


# ===============================
# MAINTENANCE TUNNEL PATH
# ===============================
def tunnel_path(inventory):
    print("\n🔦 You sneak into the dark maintenance tunnels...")
    print("SFX: *drip... drip...*")

    inventory = find_item(inventory)
    event = random.randint(1, 4)

    if event == 1:
        print("\nYou find a locked door... and a keypad!")
        print("You guess the code...")
        code = random.randint(100, 999)
        guess = input("Enter any 3-digit number: ")

        if guess == str(code):
            print("✨ You got it exactly! Door opens — you're safe!")
            return True, inventory
        else:
            print("Wrong code... but the T-Rex doesn't find you. Safe!")
            return True, inventory

    if event == 2:
        print("\nYou find an emergency ladder and climb to safety!")
        return True, inventory

    if event == 3 and "flashlight" in inventory:
        print("\nYou use your flashlight to find a hidden escape vent!")
        return True, inventory

    print("\nYou get lost in the dark...")
    print("SFX: *ROOOOOAR echoes through the tunnel*")
    return False, inventory


# ===============================
# PLAY AGAIN
# ===============================
def play_again():
    answer = input("\nPlay again? (yes/no): ").lower()
    while answer not in ("yes", "no"):
        answer = input("Type yes or no: ").lower()
    return answer == "yes"


# ===============================
# MAIN GAME LOOP
# ===============================
def main():
    intro()

    playing = True
    while playing:
        inventory = []  # reset each game

        choice = choose_path()

        if choice == "1":
            survived, inventory = jungle_path(inventory)
        elif choice == "2":
            survived, inventory = jeep_path(inventory)
        else:
            survived, inventory = tunnel_path(inventory)

        print("\nYour final inventory:", inventory)

        if survived:
            print("\n🎉 YOU ESCAPED THE T-REX! GREAT JOB! 🎉")
        else:
            print("\n💀 YOU WERE CAUGHT BY THE T-REX. TRY AGAIN! 💀")

        playing = play_again()

    print("\nThanks for playing! Goodbye! 👋")

# RUN GAME
main() 