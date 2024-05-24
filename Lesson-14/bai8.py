n = input("Input a number: ")

while not n.isdigit():
    print("\nPls input a number.")
    n = input("Input a number: ")
n = int(n)

Fibonaccis = [1, 1]
for i in range(1, n-1):
    Fibonaccis.append(Fibonaccis[i] + Fibonaccis[i-1])

print(f"First {n} Fibonacci numbers: ", Fibonaccis)