# Ana Otero
# Oct 13, 2025
# P2HW1 - Travel Budget Formatting
# This program calculates and displays travel expenses with formatted output.

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))

accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))

expenses = gas + accommodation + food
remaining = budget - expenses

print("\n------------Travel Expenses------------")

print(f"{'Location:':20}{destination}")

print(f"{'Initial Budget:':20}${budget:10.2f}")

print(f"{'Fuel:':20}${gas:10.2f}")

print(f"{'Accommodation:':20}${accommodation:10.2f}")

print(f"{'Food:':20}${food:10.2f}")

print("---------------------------------------")
print(f"{'Remaining Balance:':20}${remaining:10.2f}")