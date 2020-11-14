""" Assingment palidrome_2_old
    Created on 08-11-2020, 21:04
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string
# with user input the middle of the sentence

def front_alphabet(human):
    alphabet = ''
    for letter in range(0,  human):
        alphabet += chr(ord("a") + letter)
    return alphabet

# function to mirror front_aplhabet output
def back_alphabet(input):
    return input[::-1]

# take user input of str into ord
human = ord(input("Please enter a letter: ")) - 97


palidrome_2 = front_alphabet(human) + chr(human+97) + back_alphabet(front_alphabet(human))

print(palidrome_2)







