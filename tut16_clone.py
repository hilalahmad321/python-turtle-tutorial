import turtle

t = turtle.Turtle()
t.speed(1)

turtle.bgcolor("black")
c = t.clone()
t.color("blue")
c.color("red")
c.color("white")
t.circle(50)
c.circle(-50)
c.circle(70)
