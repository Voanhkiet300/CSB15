import turtle
t = turtle

n = int(input("Enter a number > 2 for the number of sides: "))

if n <= 2:
    print("Invalid number of sides. The number of sides must be > 2.")
else:
    t.speed(10)
    t.pencolor("black")
    t.pensize(3)

    angle = 180-((n-2)*180)/n

    for i in range(n):
        t.forward(100)
        t.left(angle)

    t.done()