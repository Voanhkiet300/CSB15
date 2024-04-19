def is_prime(n):
    if int(n) < 2:
        return False
    for i in range(2, int(int(n)**0.5) + 1):
        if int(n) % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < int(n):
        if is_prime(num):
            print(num)
            count += 1
        num += 1



n = input("Input a number: ")

print_first_n_primes(int(n))