''' Assignment: if_statement_class
    Created on 24-10-2020 05:44
    @author Alejo Cain '''

#number = int(input("Enter a number: "))

#if number < 0:
 #   number = number * - 1

#print("%d" % number)

#a = int(input("Enter a number a:"))
#b = int(input("Enter a number b:"))

#if a > b:
 #   print("%d" % a)
#else:
#    print("%d" % b)

#Exercise: Write a program that reads 3 numbers, then prints the larges of the 3

"""number1 = int(input("Enter a number "))
number2 = int(input("Enter a another number"))
number3 = int(input("Enter the last number")) """

"""if number1 > (number2 and number3):
    print("%d" % number1)
elif number2 > (number1 and number3):
    print("%d" % number2)
elif number3 > (number1 and number2):
    print("%d" % number3)"""
# used elif statements too soon it can also be done as following
"""if number1 > number2 and number1 > number3:
    print("%d" % number1)
else:
    if number2 > number3:
        print("%d" % number2)
    else:
        print("%d" % number3)"""
# using elif is better :)
"""if number1 > number2 and number1 > number3:
    print("%d" % number1)
elif number2 > number3:
    print("%d" % number2)
else:
    print("%d" % number3)"""
#this is a little bit more compact

"""write a program that reads a positive integeer, then finds the correct group the number belongs to 
- if the number is lower than 10
- if the number is at least 10 and lower than 100
- if the number is at least 100 and lower than 10000
- if the number is at least 1000
Then number of the group has to be stored in a variable called group """

"""number = int(input("Enter a number: "))
group1 = 10 > number
group2 = 100 > number
group3 = 1000 > number
group4 = 1000 < number


if group1 < number:
    print("The number is %d belonging in group 1" % (number))
elif group2 > group1:
    print("The number is %d belonging in group 2" % (number))
elif group3 > group2:
    print("The number is %d belonging in group 3 " % (number))
else:
    print("The number is %d belonging in group 4" % (number))

# catch negative numbers
#if number < 0:
#       number = number * -1""" # This was terrible hahahah

"""number = int(input("Enter a number: "))

if number < 10:
    group = 1
elif number < 100:
    group = 2
elif number < 1000:
    group = 3
else:
    group = 4
print("The number is %d belonging to group %d " % (number, group))"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(" The number %d is even" % (number))
else:
    print("The number %d is odd " % (number))
