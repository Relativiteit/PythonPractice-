import turtle
wn = turtle.Screen()
color_user = input("Enter a color: ")
tess_user = input("Enter a desired color for the tess: ")
tess_pen = int(input("Enter a desired t h i c c ness for the penn: "))
wn.bgcolor(color_user)
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color(tess_user)
tess.pensize(tess_pen)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()