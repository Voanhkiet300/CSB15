list = [78, 70, 67, 56, 45]

def bai2(list):
    print("High scores:")
    for i in range(len(list)):
        print(f"{i+1}. {list[i]}")

def bai3(list):
    list.append(int(input("Input new score: ")))
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print("High scores:")
    if len(list) > 5:
        for i in range(5):
            print(f"{i+1}. {list[i]}")
    else:
        for i in range(len(list)):
            print(f"{i+1}. {list[i]}")




























n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 3 or  int(n) < 2:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 2:
    bai2(list)
else:
    bai3(list)