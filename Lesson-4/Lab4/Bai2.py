n = float(input("Enter a number: "))

while n <= 0:
    if n < 0:
        print("Error: The number must be positive.")
    else:
        print("Error: The number must be greater than 0.")
    n = float(input("Enter a number: "))

print("Thank you!")