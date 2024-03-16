import turtle
t = turtle

t.pencolor("black")

r = 2
alpha = 15

t.speed(0)

while r < 200:
    t.circle(r, alpha)
    r = r + 1

t.done()