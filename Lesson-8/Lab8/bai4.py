
def a(n):
    multiplication = 1
    for i in range(int(n)):
        multiplication *= i+1
    return multiplication




n = input("Enter a number: ")

sum = 0
for i in range(int(n)):
    sum += a(i+1)/(i+1)

print("Result:", sum)