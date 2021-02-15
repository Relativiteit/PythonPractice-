""" object-oriented prorgamming
    Created oon 15/02/2021
    @author Alejo Cain """

class Point:
    """ Point class respresents and manupulates x, y coords."""

    def __init__(self):
        """ Creat a new point at he origin"""
        self.x = 0
        self.y = 0

p = Point() # Instantiate an object of type Point
q = Point() # Make a second point

print(p.x, p.y, q.x, q.y)

p.x = 7
p.y = 6

def distance_from_origin(self):
    """ Compute my disctance from the origin """
    return ((self.x **2) + (self.y **2)) ** 0.5

def print_point(pt):
    print("({0}, {1}".format(pt.x, pt.y))

def __str__(self):
    return "({0}, {1})".format(self.x, self.y)
def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

def halfway(self, target):
    """ Return the halfway point between myself and the target """
    mx = (self.x + target.x)/2
    my = (self.y + target.y)/2
    return Point(mx, my)



