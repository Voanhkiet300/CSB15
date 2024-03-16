n = int(input("Input number: "))

if n < 0:
    print("Invalid")
else:
    fact = 1
    for i in range(n):
        fact *= i + 1
    print(f"The factorial of {n} is {fact}.")