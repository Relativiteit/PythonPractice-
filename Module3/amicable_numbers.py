""" Assignment amicable_numbers
    Created on 27-10-2020,  12:04
    @author Alejo Cain """
# Program to check if the numbers are amicable
# Amicable numbers are two different numbers related in such a way
# that the sum of the proper divisors of each is equal to the other number.
def sum_proper_divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i

    return result

def is_perfect(n):
    return sum_proper_divisors(n) == n

#print(is_perfect(28))


def amicable(a, b):
    return sum_proper_divisors(a) == b and sum_proper_divisors(b) == a

print(amicable(220, 284))