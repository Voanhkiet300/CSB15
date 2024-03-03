import math

radius = float(input("Enter the radius of the circle: "))


Perimeter = 2 * math.pi * radius

area = math.pi * radius ** 2

print(f"Circumference of the circle: {Perimeter:.5f}")
print(f"Area of the circle: {area:.5f}")