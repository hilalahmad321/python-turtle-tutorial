import turtle

turtle.bgcolor("black")

t = turtle.Turtle()
a = 1
# for i in range(5):
while a < 300:
    for colors in ["blue", "red", "yellow", "green", "white"]:
        t.speed(0)
        t.circle(a)
        t.circle(-a)
        t.color(colors)
        a += 5
turtle.hideturtle()
