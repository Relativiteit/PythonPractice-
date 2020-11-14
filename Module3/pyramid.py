""" Assignment pyramid
    Created on 14-11-2020, 07:14
    @author Alejo Cain """
# write a program that prints a pyramid in the middle of the screen
# use functions with parameters
import sys
sys.setrecursionlimit(29)
i = 0
def pyramid():
    global i
    i += 1

    print(chr(ord("a")+ i,))
    pyramid()

print(pyramid())


"""
print("Print equilateral triangle Pyramid using stars ")
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")
"""



