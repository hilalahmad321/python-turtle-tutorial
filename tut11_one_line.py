import turtle

t = turtle.Turtle()

t.pencolor("red")
t.fillcolor("blue")
t.pensize(20)
# t.shapesize(10, 10, 6)
t.speed(1)
t.begin_fill()
t.circle(100)
t.circle(50)
t.circle(0)
t.circle(-100)
t.circle(-50)
t.end_fill()

# t.pen(pencolor="blue",fillcolor="red",speed=1,pensize=20)
# t.begin_fill();
# t.circle(100)
# t.end_fill()
