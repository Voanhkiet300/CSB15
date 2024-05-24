list = [5, 1, 8, 92, -1, 30]

print("\nOriginal list:")
for i in list:
    print(i, end=' ')

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print("\nSorted list:")
for i in list:
    print(i, end=' ')