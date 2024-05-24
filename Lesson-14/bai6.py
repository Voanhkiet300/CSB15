n = input('Input a number: ')

while not n.isdigit():
    print("\nPls input a number.")
    n = input("Input a number: ")



print(f"This number has {len(n)} digit(s).")