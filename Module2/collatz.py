""" Assignment collatz
    Created on 14-11-2021, 14:26
    @author Alejo Cain """

# Get user input
n = int(input("lease enter a positive integer: "))

# Perform the actions below until n is equal to 1.
while n != 1:  # if not equal it returns True and when it's True it will do the loop :)

    # If n is divisible by 2 then divide n by 2.
    if n % 2 == 0:  # if the rest of number divided by 2 is 0 then divide n by 2
        n /= 2  # n = n / 2
    # If n is not divisible by 2 then multiply by 3 and add one to the result.
    else:
        n = (n * 3) + 1
    # Print the value of n at the end of every loop
    print("%d" % n)
