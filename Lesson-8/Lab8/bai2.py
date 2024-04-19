def is_prime(n):
    if int(n) < 2:
        return False
    for i in range(2, int(int(n)**0.5) + 1):
        if int(n) % i == 0:
            return False
    return True

num = input("Input a number: ")

if is_prime(num):
    print(f'{int(num)} is a prime')
else:
    print(f'{num} is not a prime')