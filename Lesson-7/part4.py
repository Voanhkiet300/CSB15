import random

list = []
for i in range(5):
    list.append(str(random.randint(1, 100)))


def bai1(list):
    print("Original List: ", ', '.join(list))
    print("Even numbers: ", end=' ')
    for i in range(len(list)):
        if int(list[i]) % 2 == 0:
            print(list[i], end=' ')

def bai2(list):
    list = []
    print("Input the list of numbers.\nEnter 0 to finish.")
    a = input()
    while a != "0":
        list.append(a)
        a = input()
    for i in range(len(list)):
        if int(list[i]) % 2 == 0:
            print(list[i], end=' ')


















n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 2 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    bai1(list)
else:
    bai2(list)