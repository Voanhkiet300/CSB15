list = []

n = input("Number of items: ")
while not n.isdigit():
    n = input("Invalid input. Please enter a number: ")

for i in range(int(n)):
    item = input(f"Item {i+1}: ")
    price = input(f"Price of item {i+1}: ")
    list.append((item, float(price)))

sum = 0
for i in range(int(n)):
    sum += list[0][1]
average = sum/2
print(f"Average price: {average}")
print("Item(s) above average price: ", end='')
for i in range(int(n)):
    if list[i][1] > average:
        print(f"({list[i][0]}: {list[i][1]}), ", end="")