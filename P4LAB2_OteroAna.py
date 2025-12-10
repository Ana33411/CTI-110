# Ana Otero
# P4LAB2 - Multiplication Table
# This program displays a multiplication table for a positive integer using loops.

def multiplication_table():
    while True:

        num = int(input("Enter an integer: "))

        if num < 0:
            print("This program does not handle negative numbers.\n")
        else:

            for i in range(1, 13):
                print(f"{num} * {i} = {num * i}")
            print()  

        again = input("Would you like to run the program again? ").strip().lower()

        while again not in ("yes", "no"):
            again = input("Please enter 'yes' or 'no': ").strip().lower()

        if again == "no":
            print("\nExiting program...")
            break
        else:
            print()  

multiplication_table()