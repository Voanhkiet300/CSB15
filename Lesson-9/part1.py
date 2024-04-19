def bai1():
    def check(num):
        if num % 2 == 0:
            return True
        else:
            return False

    num = int(input("Enter a number: "))
    if check(num):
        print("This number is even")
    else:
        print("This number is not even")



def bai2():
    def cal_area(r):
        return 3.14 * r * r

    r = float(input("Enter the radius: "))
    print("The area of the circle is: ", cal_area(r))


def bai3():
    def reverse_str(t):
        return t[::-1]

    t = input("Enter a text: ")
    print("The reversed text: ", reverse_str(t))




def bai4():
    def is_palindrome(s):
        return s == s[::-1]

    if is_palindrome(s):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")











n = input("Nhập bài muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 4 or  int(n) < 1:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    bai1()
elif n == 2:
    bai2()
elif n == 3:
    bai3()
else:
    bai4()