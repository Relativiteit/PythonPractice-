import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")


tess = turtle.Turtle()
tess.shape("square")
tess.color("hotpink")
tess.pensize(5)
tess.speed(2)

alex = turtle.Turtle()
alex.shape("turtle")
alex.speed(2)

for i in range(3):
    tess.forward(80)
    tess.left(120)

tess.forward(80)
tess.right(120)

for c in ["yellow", "red", "purple", "blue" ]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)

alex.penup()
alex.forward(100)
alex.pendown()



