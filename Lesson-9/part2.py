def bai1():
    def a(n):
        multiplication = 1
        for i in range(int(n)):
            multiplication *= i+1
        return multiplication

    n = input("Input a number: ")
    while not n.isdigit():
        n = int(input("Nhập lại bài muốn chạy: "))
    n = int(n)
    print(f"{n}! = {a(n)}")




def bai2():
    a = [5, 1, 8, 92, -1, 30]

    print("Original list:")
    for i in range(len(a)):
        print(a[i], end=" ")

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    print("\nSorted list:")
    for i in range(len(a)):
        print(a[i], end=" ")



def bai3():
    def print_fibo(n):
        global a
        a = [1, 1]
        for i in range(n):
            a.append(a[i+1] + a[i])
        for i in range(n):
            print(a[i], end=" ")


    n = input("Input a number: ")
    while not n.isdigit():
        n = input("Input a number: ")
    n = int(n)
    while n <= 0:
        n = input("Input a number: ")
    print(f"First {n} Fibonacci numbers:")
    print_fibo(n)





n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 3 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    bai1()
elif n == 2:
    bai2()
else:
    bai3()