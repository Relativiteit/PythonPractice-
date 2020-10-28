""" Assignment whilte_loops
    Created on 25-10-2020, 12:27
    @author Alejo Cain """
"""#state variable
i = 1
#state while condition when 1 is smaller than 10
while i <= 10:
    print("%d" % i)
    i = i + 1 # add 1 to i using it as a counter """

"""#Exercise, read a number n, then print all squares(0^2, 1^2, 2^2) smaller than n squared
n = int(input("Enter a number: "))
i = 0
while i < n:
    print("%d" % i ** 2)

    i = i + 1"""

#Exercise, read a number n, then print the largest square smaller than n
n = int(input("Enter a number: "))
i = 0

while i ** 2  < n:
             # but if the i = i + 1 statement is here then you need to change the print function to (i-1) ** 2
    print("%d" % i  ** 2)
    i = i + 1 # if the i = i + 1 statement is here the code will work normally

