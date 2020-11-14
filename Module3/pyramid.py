""" Assignment pyramid
    Created on 14-11-2020, 07:14
    @author Alejo Cain """
# write a program that prints a pyramid in the middle of the screen
# use functions with parameters
INDEX_LETTER = 30

def front_aplhabet(human):
    alphabet = ''
    for letter in range(ord("a"), (human)):
        alphabet += chr(letter) # range(122, 97 -1 , -1 )
    for letter in range((human), ord("a")-1,-1): # the -1 after "a" makes it 96
        alphabet += chr(letter)
    return alphabet

def place_of_middle_string(lenght, palindrome):
    start_index = int(lenght/2 - len(palindrome)/2)
    space = ""
    for i in range(0, start_index):
        space += " "

    space += palindrome
    last_spacebars = lenght - len(space)
    for i in range(0, last_spacebars):
        space += " "

    return space

for i in range(ord("a"), ord("p")):
    palindrome = front_aplhabet(i)

    print(place_of_middle_string(INDEX_LETTER, palindrome))






