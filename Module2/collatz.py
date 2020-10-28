""" Assignment collatz
    Created on 25-10-2020, 14:41
    @author ALejo Cain """
"""#Input of user
number = int(input("Enter a positive number: "))

while number !=1:
    if number % 2 == 0:
        number = number // 2
        print("%d is uneven with the following Collatz sequence: " % (number))

    else:
        number = (3 * number) + 1
        print("%d is even with the following Collatz sequence: " % (number))
#not happy with this solution not able to further the collatz sequence.

"""
"""
def collatz(n):
    while n != 1:
        if n % 2 == 0: #Number is even
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
#input useri
number = input("Enter number: ")

try:
    number = int(number)
    collatz(number)
except ValueError:
    print("Please input a valid value")
#This works however we have not learned about classes/methods yet so I guess it does not count."""

#code after consulting a friend 27-10-2020

#Get user input
n = int(input("lease enter a positive integer: "))

#Perform the actions below untill n is equal to 1.
while n != 1: #if not equal it returns True and when it's True it will do the loop :)

    #If n is divisble by 2 then divide n by 2.
    if n % 2 == 0: #if the rest of number devided by 2 is 0 then devide n by 2
        n /= 2 # n = n / 2
    #If n is not divisible by 2 then multiply by 3 and add one to the result.
    else:
        n = (n * 3) + 1
    #Print the value of n at the end of every loop
    print("%d" % n)