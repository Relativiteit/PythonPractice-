""" Assignment factorial_n
    Created on 27-10-2020,  11:44
    @author Alejo Cain """

# if year is divisible by 4 else statement
# except if year is divisible by 100 elif statement
# except if year is divisible by 400 if statement
#define function with parameter
def is_leap_year(year): #boolian function
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

year = int(input("Enter a year: "))

if is_leap_year(year):
    print("The year %d is a leap year" % year)
else:
    print("The year %d is not a leap year" % year)