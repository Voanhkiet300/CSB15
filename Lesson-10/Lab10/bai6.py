n = input("Input sequence: ")
count = {}

for char in n:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(f"Frequency of characters:\n{count}")