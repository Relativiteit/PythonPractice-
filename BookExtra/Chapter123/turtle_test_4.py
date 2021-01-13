import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for i in range(30):
    tess.stamp()        # leaves an impression on the canvas
    tess.color("hotpink")# to see contrast of mirror images
    size = size + 3     # increase the size on every iteration
    tess.forward(size)  # move tess along
    tess.right(24)      # ... turn her

tess.color("blue")
alex = turtle.Turtle()
alex.penup()
alex.forward(100)
alex.pendown()

wn.mainloop()