import turtle

t = turtle.Turtle()

t.color("red", "blue")
a = 10
while (a < 100):
    t.speed(10)
    t.circle(a)
    t.circle(-a)
    a += 10
