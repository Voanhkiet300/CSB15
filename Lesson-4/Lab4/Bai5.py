numbers = []

def sum_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

for i in range(1000, 10000):
    if sum_digits(i) == 9:
        numbers.append(i)
        if len(numbers) == 10:
            print("The first 10 numbers with a sum of digits equal to 9 are:")
            print(numbers)
        