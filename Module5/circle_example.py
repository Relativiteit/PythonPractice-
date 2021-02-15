""" circle_example
    Created on 11/02/2021
    @author Alejo Cain """

import math
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def cirumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

def show (circle):
    a = circle.centre.x
    b = circle.centre.y
    c = circle.radius
    print("The x coordinate is %.2f and the y coordinate is %.2f with a circle radius of %.2f" % (a,b,c))

def read_circle(line):
    data = map(float(line.split()))
    centre = Coordinate(data[0], data[1])
    radius = data[0]
    return Circle(centre, radius)


centre = Coordinate(12.45, 34.98)
circle = Circle(centre, 2.001)
show(circle)
print( "The area is %f" % circle.area())


""" read_circle(raw_input("give circle: " show(c) """

file = open("circles")
lines = file.readlines()
c1 = read_circle(lines[0])
'1.5, 4.6 '
c2 = read_circles9lines[1]
if c1.bigger_than(c2):
    c = c1
else:
    c = c2
print("The area of the biggesst circle is %f" % c.area())