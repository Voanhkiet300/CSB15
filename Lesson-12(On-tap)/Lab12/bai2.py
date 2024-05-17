import os

n = input("Input file name:")


if os.path.exists(n):
    if os.path.isfile(n):
        with open(n, 'r') as file:
            a = file.read()
            print(f'File content:\n{a}')
    elif os.path.isdir(n):
        print('File not found.')
else:
    print('File not found.')
