computer = {'HP': 20, "DELL": 50, 'MACBOOK': 12, "ASUS": 30}

# Phan 1:

# bai 2:
def bai2p1():
    print("Available MACBOOKs:", computer['MACBOOK'])

# bai 3:
def bai3p1():
    a = input("Input a brand: ")
    if a in computer:
        print(f"Available {a}s:", computer[a])
    else:
        print("Not available")


# Phan 2:

# bai 1:
def bai1p2():
    computer.update({"TOSHIBA": 10})
    print("Available products:")
    for key, value in computer.items():
        print(f"{key}: {value}")

# bai 2:
def bai2p2():
    a = input("Input a brand: ")
    b = input("Input amount: ")
    computer.update({f"{a}": b})

    print("Available products:")
    for key, value in computer.items():
        print(f"{key}: {value}")

# bai 3:
def bai3p2():
    computer["DELL"] = 60
    computer["MACBOOK"] = 2
    print("Available products:")
    for key, value in computer.items():
        print(f"{key}: {value}")

# bai 4:
def bai4p2():
    sum = 0
    for i in computer.values():
        sum += i

    print("Total products:", sum)



def phan1():
    
    n = input("Nhập bài muốn chạy(2, 3): ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    while int(n) > 3 or  int(n) < 2:
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    if n == 1:
        bai2p1()
    else:
        bai3p1()

def phan2():
    n = input("Nhập bài muốn chạy(1, 2, 3, 4): ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    if n == 1:
        bai1p2()
    elif n == 2:
        bai2p2()
    elif n == 3:
        bai3p2()
    else:
        bai4p2()


n = input("Nhập phần muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 2 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    phan1()
else:
    phan2()