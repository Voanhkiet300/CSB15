import random

list = []
for i in range(5):
    list.append(str(random.randint(1, 100)))



def bai1(list):
    print("Original List: ", ', '.join(list))
    num = input("Input a number: ")
    while not num.isdigit() or int(num) > 100:
        num = input("Input a number: ")
    for i in range(len(list)):
        if list[i] == num:
            print(f"Number found at position {i+1}")
            return 0
    print("Number not found")

def bai2(list):
    print("Original List: ", ', '.join(list))
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    print("Sum of all numbers:", sum)

def bai3(list):
    list = []
    sum = 0
    print("Input the list of numbers.\nEnter 0 to finish.")
    a = input()
    while a != "0":
        list.append(a)
        a = input()
    for i in range(len(list)):
        sum += int(list[i])
    print("Sum of numbers in list:", sum)























n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 3 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    bai1(list)
elif n == 2:
    bai2(list)
else:
    bai3(list)