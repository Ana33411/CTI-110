# Ana Otero
# October 15, 2025
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal.

money = float(input("Enter amount of money: "))

cents = int(round(money * 100))

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