vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()  # line 2
print(keys)
print()

vehicle = input("Enter a vehicle to see its mpg: ") 

if vehicle not in vehicles:
    print()
    print(f"Error: '{vehicle}' is not in the dictionary. Please enter one of the keys exactly as shown above.")
    sys.exit(1)

mpg = vehicles[vehicle]

print()

print(f"The {vehicle} gets {mpg} mpg.")

print()

try:
    miles = float(input(f"How many miles will you drive the {vehicle}? "))

except ValueError:
    print()
    print("Error: please enter a numeric value for miles.")
    sys.exit(1)

gallons_needed = miles / mpg

print()