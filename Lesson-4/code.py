input = input("your input: ")

def my_uppercase(str):
    distance = ord('A') - ord('a')
    for ch in str:
        if ch > 'a' and ch < 'z':
            print(chr(ord(ch) + distance), end="")
        else:
            print(ch, end="")


# for
import random
my_list = ["apple", "banana", "cherry"]

random_list = random.choices(my_list, k=3)
print(random_list)

for i, item in enumerate(random_list, start=1):
    print(f"{i}. {item}")