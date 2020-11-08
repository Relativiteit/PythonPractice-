""" Assingment palidrome_1
    Created on 08-11-2020, 08:23
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string

def front_aplhabet():
    alphabet = ''
    for letter in range(0, 25):
        alphabet += chr(ord("a") + letter)
    return alphabet

# function to mirror front_aplhabet output
def back_alphabet(input):
    return input[::-1]

def end_aplhabet():
    alphabet ='' # could have used end = '' too
    for letter in range(25,26):
        alphabet += chr(ord("a")+ letter)
    return alphabet

palidrome = front_aplhabet() + end_aplhabet() + back_alphabet(front_aplhabet())
print(palidrome)






