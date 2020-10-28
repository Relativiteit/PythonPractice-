""" Assignment string_splitting
    Created on 25-10-2020, 20:12
    @author Alejo Cain """
"""#little program to count howmany words in a sentence 
sentence = input("Enter a sentence: ")
words = sentence.split()

print("%d" % len(words))"""

#program to count integers and calculate sum
input_numbers = (input("Enter a random amount of numbers with a space inbetween: "))
#you can give the .split() function a parameter to split uppon default is (multiple)space but you can choose whatever
#example .splitt(":") now it will split input in the formate a:b:c to ['a','b','c']
numbers = input_numbers.split()

sum = 0
#for i in range (i = extra) range = the input
for extra in numbers:
    sum = sum + int(extra)

print("%d " % sum)

