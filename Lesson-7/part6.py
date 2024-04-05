list1 = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
list2 = [247100, 333300, 266800, 420900, 318000]
list3 = [9.224, 43.35, 12.04, 9.96, 10.09]
list4 = []



for i in range(len(list1)):
    list4.append(list2[i] / list3[i])

def bai1(list1, list2, list3, list4):
    print("Popluation density of:")
    for i in range(len(list1)):
        print(f"{list1[i]}: {list4[i]}")

def bai2(list1, list2, list3, list4):
    tong = 0
    for i in range(len(list1)):
        tong += list4[i]
    print("Average population  density: ", tong/len(list1))




















n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 2 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    bai1(list1, list2, list3, list4)
else:
    bai2(list1, list2, list3, list4)