def is_int(num):
    if num.isdigit() and int(num) % 1 == 0:
        return True
    else:
        return False

num = input('Enter a number: ')

if is_int(num):
    print(f'{int(num)} is an integer')
else:
    print(f'{num} is not an integer')