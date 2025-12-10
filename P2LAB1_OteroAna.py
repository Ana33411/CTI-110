import math

try:
    radius = float(input("What is the radius of the circle? "))

except ValueError:
    print("Please enter a valid number for the radius.")

else:
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    print()

    print(f"The diameter of the circle is {diameter:.1f}")
    print()

    print(f"The circumference of the circle is {circumference:.2f}")
    print()
    
    print(f"The area of the circle is {area:.3f}")