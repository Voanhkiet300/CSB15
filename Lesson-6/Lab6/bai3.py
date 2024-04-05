n = input("Input a positive number: ")
while not n.isdigit() or int(n) <= 0:
    n = input("Input a positive number: ")
a = [1, 1]
print(f"First {n} Fibonacci number(s): ", end='')
for i in range(1, int(n)+1):
    a.append(a[-2]+a[-1])
for i in range(int(n)):
    print(a[i], end=' ')