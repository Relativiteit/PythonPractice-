""" Assignment video 11 split_sentence
    Created on 26-10-2020
    @author Alejo Cain """

"""sentence = input("Enter a sentence: ")
words = sentence.split()
print("%d" % len (words)) """

"""'numbers = input("Enter some numbers: ")
numbers = numbers.split()
print(numbers)
# ["11", "12", "13"]"""
"""
numbers = input("Enter some numbers: ")
numbers = numbers.split()

sum = 0

for i in numbers:
    sum = sum +int(i)
print("%d" % sum)
# ["11", "12", "13"] """
"""
l = input("Enter some values: ").split()

l[0]
#start at 2 stop at lenght l and stepsize 2
for i in range(2, len(l), 2):
    print(l[i])
"""
l = input("Enter some values: ").split()
#print the list starting at element 0 and ending at the lenght of the list
for i in range(0, len(l), 2):
    print(l)
