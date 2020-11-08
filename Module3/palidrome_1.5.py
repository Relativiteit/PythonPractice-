""" Assingment palidrome_1.5
    Created on 08-11-2020, 14:23
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string
# with user input the middle of the sentence

def front_aplhabet():
    alphabet = ''
    for letter in range(0, 26):
        alphabet += chr(ord("a") + letter)
    return alphabet

# function to mirror front_aplhabet output
def back_alphabet(input):
    return input[::-1]

def end_aplhabet():
    alphabet ='' # could have used end = '' too
    for letter in range(25,26):
        alphabet += chr(ord("a") + letter)
    return alphabet
def user_input():
    human = (input("Please enter a letter: "))
    return human



palidrome_2 = front_aplhabet() + user_input() + back_alphabet(front_aplhabet())
print(palidrome_2)







