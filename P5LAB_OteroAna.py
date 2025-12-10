# Ana Otero
# November 30, 2025
# P5LAB
# This program simulates a self-checkout machine displaying dollars and coins.

import random

def disperse_change(change):

    cents = int(round(change * 100))

    dollars = cents // 100
    cents -= dollars * 100

    quarters = cents // 25
    cents -= quarters * 25

    dimes = cents // 10
    cents -= dimes * 10

    nickels = cents // 5
    cents -= nickels * 5

    pennies = cents

    if dollars > 0:
        print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")
    if quarters > 0:
        print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")
    if dimes > 0:
        print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")
    if nickels > 0:
        print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")
    if pennies > 0:
        print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")


def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change}")

    print() 

    disperse_change(change)


main()