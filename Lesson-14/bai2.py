from math import *


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

delta = b**2 - 4*a*c


if delta < 0:
    print("The equation has no solution")
elif delta == 0:
    x = -b / (a*2)
    print("The equation has 1 solutions.")
    print(f"x = {x}")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    print("The equation has 2 solutions.")
    print(f"x = {x1} or x = {x2}")