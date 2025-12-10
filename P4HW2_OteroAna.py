# Ana Otero
# Date: October 31, 2025
# P4HW2 – Payroll Calculator for Multiple Employees
# This program calculates gross pay for multiple employees including overtime.
# The user can continue entering employee data until “Done” is entered.
# At the end, the program displays total overtime, total regular pay, total gross 
pay, and employee count.
# Pseudocode:
# Initialize totals for overtime pay, regular pay, and gross pay
# Ask for hours worked and pay rate
# Calculate overtime hours (if > 40)
# Compute gross pay = regular + overtime
# Display individual results in formatted table
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0
while True:
 name = input('Enter employee\'s name or "Done" to terminate: ')
 if name.lower() == "done":
 break
 hours = float(input(f'How many hours did {name} work? '))
 rate = float(input(f'What is {name}\'s pay rate? '))
 if hours > 40:
 overtime_hours = hours - 40
 overtime_pay = overtime_hours * (rate * 1.5)
 regular_pay = 40 * rate
 else:
 overtime_hours = 0
 overtime_pay = 0
 regular_pay = hours * rate
 gross_pay = regular_pay + overtime_pay
 print(f"\nEmployee name: {name}")
 print("---------------------------------------------------------------")
 print("Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross 
Pay")
 print("---------------------------------------------------------------")
 print(f"{hours:<13.1f}{rate:<11.2f}{overtime_hours:<11.1f}{overtime_pay:<15.2f}
${regular_pay:<14.2f}${gross_pay:<.2f}\n")
 total_overtime_pay += overtime_pay
 total_regular_pay += regular_pay
 total_gross_pay += gross_pay
 employee_count += 1
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")