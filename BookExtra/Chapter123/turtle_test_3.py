import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

for i in range(3):
    tess.forward(80)
    tess.left(120)

tess.forward(80)
tess.right(120)

for c in ["yellow", "red", "purple", "blue" ]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)