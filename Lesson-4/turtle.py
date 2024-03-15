a = int(input("nhap vao so canh(>2): "))

def draw(a):
    import turtle
    t = turtle.Turtle()
    t.speed(10)

    for i in range(a):
        t.forward(100)
        t.right(180-((a-2)*180)/a)
    turtle.done()

if a>2:
    draw(a)
    