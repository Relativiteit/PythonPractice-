""" Assignment pyramid
    Created on 14-11-2020, 07:14
    @author Alejo Cain """
# write a program that prints a pyramid in the middle of the screen
# use functions with parameters


def pyramid(human, rows):
    alphabet = ''  # empty string
    human = ord(input("Please enter a letter: "))
    rows = int(input("Please enter amount of desired rows: "))

    for letter in range(ord("a"), human):
        alphabet += chr(letter)
    for letter in range(human, ord("a")-1,-1):
        alphabet += chr(letter)
    return alphabet

goat = pyramid()
print(goat)




