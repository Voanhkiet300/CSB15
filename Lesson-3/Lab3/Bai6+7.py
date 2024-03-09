

def kiem_tra_goc_vuong(a, b, c):
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return "Tam giác vuông"
    else:
        return "Không phải tam giác vuông"

def kiem_tra_tam_giac_deu(a, b, c):
    if a == b == c:
        return "Tam giác đều"
    else:
        return "Không phải tam giác đều"

def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if kiem_tra_goc_vuong(a, b, c) == "Tam giác vuông":
            return "Có thể là cạnh của một tam giác vuông"
        elif kiem_tra_tam_giac_deu(a, b, c) == "Tam giác đều":
            import turtle
            t = turtle.Turtle()
            t.speed(10)
            t.pensize(2)
            for i in range(3):
                t.forward(a*10)
                t.left(120)
            turtle.done()
            return "Có thể là cạnh của một tam giác đều"
        else:
            return "Có thể là cạnh của một tam giác bình thường"
    else:
        return "Không thể là cạnh của một tam giác"

a = float(input("Nhập vào độ dài cạnh 1: "))
if a <= 0:
    print("Vui lòng nhập vào độ dài cạnh dương")
else:
    b = float(input("Nhập vào độ dài cạnh 2: "))
    if b <= 0:
        print("Vui lòng nhập vào độ dài cạnh dương")
    else:
        c = float(input("Nhập vào độ dài cạnh 3: "))
        if c <= 0:
            print("Vui lòng nhập vào độ dài cạnh dương")
        else:
            print(check(a, b, c))


