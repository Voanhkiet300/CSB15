list1 = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
list2 = [247100, 333300, 266800, 420900, 318000]

def bai2(list2):
    min = 1000000000
    max = 0
    for i in range(len(list2)):
        if list2[i] < min:
            min = list2[i]
        if list2[i] > max:
            max = list2[i]
    print(f"Indices of:\nMost populated dist: {min}\nLeast populated dist: {max}")

def bai3(list1, list2):
    min = 1000000000
    max = 0
    for i in range(len(list2)):
        if list2[i] < min:
            min = list2[i]
        if list2[i] > max:
            max = list2[i]
    print(f"Names of:\nMost populated dist: {list1[list2.index(min)]}\nLeast populated dist: {list1[list2.index(max)]}")





















n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 3 or  int(n) < 2:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 2:
    bai2(list2)
else:
    bai3(list1, list2)