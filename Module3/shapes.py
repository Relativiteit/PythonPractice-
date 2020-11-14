""" Assignment recursion
    Created on 14-11-2020, 09:35
    @author Alejo Cain """

# practice shapes
import sys
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i +=1
    print("Hello", i)
    greet()

greet()
