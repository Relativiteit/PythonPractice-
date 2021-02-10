""" a_find_function
    Created on 10/02/2021 09:58
    @author Alejo Cain """

def find(strng, ch):
    """
        Find and return the index of ch in strng.
        Return -1 if ch does not ccur in strng.
    :param strng: can be any word
    :param ch: specific letter
    :return: -1 if param ch is not found
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(find("Compsci", "p") == 3)
print(find("Compsci", "C") == 0)
print(find("Compsci", "i") == 6)
print(find("Compsci", "x") == -1)
