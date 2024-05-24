a = input("Input first number: ")
while not a.isdigit():
    print("\nPls input a number.")
    a = input("Input first number: ")
a = int(a)
b = input("Input second number: ")
while not b.isdigit():
    print("\nPls input a number.")
    b = input("Input second number: ")
b = int(b)

print(a, "+", b, "=", a+b)