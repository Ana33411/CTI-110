# Ana Otero
# October 2025
# P3HW2
# Program calculates employee pay, including overtime, with formatted output

# Pseudocode:
# Ask for employee name
# Ask for hours worked
# Ask for pay rate
# Display all results formatted in columns

name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
 overtime_hours = hours_worked - 40
 overtime_pay = overtime_hours * (pay_rate * 1.5)
 reg_pay = 40 * pay_rate

else:
 overtime_hours = 0
 overtime_pay = 0
 reg_pay = hours_worked * pay_rate
gross_pay = reg_pay + overtime_pay

print("----------------------------------------")

print(f"Employee name: {name}")

print("Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross 
Pay")

print("---------------------------------------------------------------")

print(f"{hours_worked:<15.1f}
{pay_rate:<10.1f}{overtime_hours:<10.1f}
{overtime_pay:<15.2f}${reg_pay:<12.2f}${gross_pay:<.2f}")