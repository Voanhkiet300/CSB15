from turtle import *


# pen
color("red")
pensize(2)

speed(10)

# direction
up()
backward(300)
down()

# ngu giac
for i in range(5):
    forward(100)
    left(72)

up()
setpos(0, 0)
down()

# ngoi sao
color("yellow")
left(36)
for i in range(5):
    forward(200)
    left(144)


up()
backward(350)
down()

# hinh tam giac
color("blue")
right(36)
for i in range(3):
    forward(150)
    left(120)

up()
forward(300)
down()

# hinh tron
color("green")
circle(radius=80)



mainloop()