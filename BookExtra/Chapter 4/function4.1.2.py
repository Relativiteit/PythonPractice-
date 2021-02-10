import turtle
__import__("turtle").__traceable__= False
# test
def draw_multicolor_square(t, sz):
      #Make turtle t draw a multi-color square of sz
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(10):
    draw_multicolor_square(tess, size)
    size = size + 4
    tess.forward(10)
    tess.right(18)


def draw_multicolor_triangle(j, tr):
    # Make turtle j draw a multi0color triangle of tr
    for i in ["pink", "blue", "green"]:
        j.color(i)
        j.forward(tr)
        j.left(120)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
Amor = turtle.Turtle()
Amor.pensize(3)

size = 20

for i in range(15):
    draw_multicolor_triangle(Amor, size)
    size = size + 3
    Amor.forward(10)
    Amor.right(18)

def draw_rectangle(t,w, h):
    """ Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


wn.mainloop()
