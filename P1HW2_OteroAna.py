# Ana Otero
# 09-28-2025
# P1HW2
# This program calculates the remaining travel budget after expenses.

"""
Pseudocode:
1. Ask user for their total budget
2. Ask user for travel destination
3. Ask user for gas expense
4. Ask user for accommodation expense
5. Ask user for food expense
6. Add up all expenses
7. Subtract expenses from budget
8. Display travel destination, expenses, and remaining budget
"""

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food

remaining_budget = budget - total_expenses

print("-----Travel Expenses-----")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget}")
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Balance: ${remaining_budget}")