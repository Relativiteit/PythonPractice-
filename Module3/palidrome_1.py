""" Assingment palidrome_1
    Created on 08-11-2020, 08:23
    @author Alejo Cain """
# write a program that will print the alphabet and reversed in 1 string
# changed from 3 functions to 1 functions by consulting TA
def front_aplhabet():
    alphabet = ''
    for letter in range(ord("a"), ord("z")):
        alphabet += chr(letter)
        # the -1 after "a" makes it 96 so a will be included in the mirror
        # range(122, 97 -1 , -1 )
    for letter in range(ord("z"), ord("a")-1, -1):
        alphabet += chr(letter)

    return alphabet


palidrome = front_aplhabet()
print(palidrome)






