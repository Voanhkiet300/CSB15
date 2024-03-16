
def sum_digits(n):
    if n <= 0:
        print("Invalid")
    else:
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit
            n = n // 10
        return sum
        
n = int(input("Enter a positive integer: "))
print(f"The sum of the digits in {n} is {sum_digits(n)}.")