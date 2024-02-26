from turtle import *


pensize(2)
speed(10)
up()
backward(300)
down()


# hinh tam giac
color("yellow")
for i in range(3):
    forward(150)
    left(120)



up()
setpos(0,0)
down()



# khung anh
color("black")
pensize(3)
for i in range(4):
    forward(140)
    left(90)
up()
setpos(10,10)
down()
pensize(1)
for i in range(4):
    forward(120)
    left(90)


up()
setpos(-200, -200)
down()

# hinh la
pensize(2)
for i in range(4):
    forward(100)
    left(90)
up()
setpos(-150, -150)
backward(70.7)
right(45)
down()
for i in range(4):
    forward(100)
    left(90)



mainloop()