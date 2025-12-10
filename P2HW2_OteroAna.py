# Ana Otero
# Oct 13, 2025
# P2HW2 - List Operations
# This program uses a list to store module test grades and displays summary statistics.

# Pseudocode:
# 1. Ask user to input grades for modules 1–6
# 2. Store grades in a list
# 3. Display: lowest, highest, sum, and average (2 decimal places)

grades = [
 int(input("Enter grade for Module 1: ")),
 int(input("Enter grade for Module 2: ")),
 int(input("Enter grade for Module 3: ")),
 int(input("Enter grade for Module 4: ")),
 int(input("Enter grade for Module 5: ")),
 int(input("Enter grade for Module 6: "))
]

print("\n------------Results------------")
print(f"{'Lowest Grade:':20}{min(grades)}")
print(f"{'Highest Grade:':20}{max(grades)}")
print(f"{'Sum of Grades:':20}{sum(grades)}")
print(f"{'Average:':20}{sum(grades)/len(grades):.2f}")
print("-------------------------------")