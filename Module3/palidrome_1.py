""" Assingment palidrome_1
    Created on 08-11-2020, 08:23
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string

def front_aplhabet():
    alphabet = ''
    for letter in range(ord("a"), ord("z")): # bad practice
        alphabet += chr(letter)
    for letter in range(ord("z"), ord("a")-1,-1):
        alphabet += chr(letter)

    return alphabet


palidrome = front_aplhabet()
print(palidrome)



"""# function to mirror front_aplhabet output
def back_alphabet(input):
    return input[::-1]

def end_aplhabet():
    alphabet ='' # could have used end = '' too
    for letter in range(25,26):
        alphabet += chr(ord("a")+ letter)
    return alphabet
    """""





