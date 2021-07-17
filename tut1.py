# what is library
# library is the important function and method that you can access to make program eaiser.
# turtle is python library you can make shapes
import turtle
# s = turtle.getscreen()
# print(s)
t = turtle.Turtle()
# t.left(90)
# t.backward(100)
# t.left(90)
# t.backward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)

# you can use shorthand

# t.rt(90)
# t.fd(100)
# t.lt(90)
# t.bk(100)

t.goto(100, -100)
t.goto(100, 100)
t.goto(-100, 100)
t.goto(-100, -100)
t.goto(100, 100)

t.goto(-100, 100)
t.goto(-100, -100)
t.goto(100, -100)

# t.goto(0, 0)
t.home()  # use instead of goto(0,0)
