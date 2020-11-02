""" Assignment factorial_n
    Created on 27-10-2020,  10:09
    @author Alejo Cain """
#function calculates and returns factorial of n
#function factorial with parameter n
def factorial(n):
    result = 1 # has to be a positive number you can't begin at 0 because 0 * n = 0

    for i in range(1, n + 1): # range starting at 1 and ending at n + 1, the + 1 or it would not be included
        result *= i # result = result * i

    return result

print(factorial(5))
print( 5 * 4 * 3 * 2 * 1)

