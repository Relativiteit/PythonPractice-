""" Assingment palidrome_2
    Created on 14-11-2020, 06:52
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string
# with user input the middle of the sentence


def front_aplhabet():
    alphabet = ''
    human = ord(input("Enter 1 letter: "))
    for letter in range(ord("a"), human):
        alphabet += chr(letter) # range(122, 97 -1 , -1 )
    for letter in range(human, ord("a")-1,-1): # the -1 after "a" makes it 96
        alphabet += chr(letter)

    return alphabet


palidrome = front_aplhabet()
print(palidrome)









