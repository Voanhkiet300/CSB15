import turtle
list = ["red", "blue", "Yellow"]



def bai1(list):
    print(f"color list:\n{' '.join(list)}")
    position = input("Input position: ")
    while not position.isdigit() or int(position) > len(list):
        position = input("Input position: ")
    position = int(position) - 1
    print(f"Color at position {position}: {list[position]}")

def bai2(list):
    print(f"color list:\n{' '.join(list)}")
    item = input("Item to delete: ")
    while (not item.isdigit() and item.isalpha()):
        item = input("Item to delete: ")
    if item.isdigit():
        index = int(item) - 1
        del list[index]
        print("New color list:", ' '.join(list))
    else:
        list.remove(item)
        print("New color list:  \n' '".join(list))

def bai3(list):
    list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    t = turtle
    t.pensize(3)
    for i in range(len(list)):
        t.pencolor(list[i])
        t.forward(15)
        t.up()
        t.forward(15)
        t.down()
    t.done()
        



















        

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