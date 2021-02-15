""" dice_throwing
    Created on 10/02/2021
    @author Alejo Cain """
import random
class Dice:
    def __init__(self, n):
        self.NUMBER_OF_FACES = n
        self.number_of_dots = 1

    def throw (self):
        self.number_of_dots = random.randint(1, self.NUMBER_OF_FACES)

d1 = Dice(6)
d2 = Dice(12)

d1.throw()
d2.throw()

print(d1.number_of_dots)
print(d2.number_of_dots)
