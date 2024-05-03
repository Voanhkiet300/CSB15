computer_price = {'HP': 600, "DELL": 650, 'MACBOOK': 1200, "ASUS": 400}
computer_amount = {'HP': 20, "DELL": 50, 'MACBOOK': 12, "ASUS": 30}

# bai 2:
def bai2p3():
    print("Price of ASUS:", computer_price["ASUS"])

# bai 3:
def bai3p3():
    a = input("Input a brand: ")
    print(f"Price of {a}: {computer_price[a]}")


# Phan 4:

# bai 1:
def bai1p4():
    print("Total price:", computer_price["ASUS"]*5)

# bai 2:
def bai2p4():
    a = input("Input a brand: ")
    b = input("Input amount to buy: ")
    print("Total price:", computer_price[a]*int(b))

# bai 3:
def bai3p4():
    a = input("Input a brand: ")
    b = input("Input amount to buy: ")
    print("Total price:", computer_price[a]*int(b))

    computer_amount[a] -= int(b)
    print("\nAvailable products:")
    for key, value in computer_amount.items():
        print(f"{key}: {value}")

# Phan 5:

# bai 1:
def bai1p5():
    print("Total value of available brands:")
    print("\nAvailable products:")
    for key, value in computer_amount.items():
        print(f"{key}: {value*computer_price[key]}")

# bai 2:
def bai2p5():
    sum = 0
    for key, value in computer_amount.items():
        sum += value*computer_price[key]
    print("\nTotal value of available items:", sum)












def phan3():
    
    n = input("Nhập bài muốn chạy(2, 3): ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    while int(n) > 3 or  int(n) < 2:
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    if n == 1:
        bai2p3()
    else:
        bai3p3()

def phan4():
    n = input("Nhập bài muốn chạy(1, 2, 3): ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    if n == 1:
        bai1p4()
    elif n == 2:
        bai2p4()
    else:
        bai3p4()

def phan5():
    n = input("Nhập bài muốn chạy(1, 2): ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    if n == 1:
        bai1p5()
    else:
        bai2p5()


n = input("Nhập phần muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 5 or  int(n) < 3:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 3:
    phan3()
elif n == 4:
    phan4()
else:
    phan5()