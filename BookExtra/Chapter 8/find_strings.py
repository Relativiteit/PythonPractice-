""" find_strings
    Created on 10-02-2021
    @author Alejo Cain """

ss = "Python strings have some interesting methods."

print(ss.find("s") == 7)
print(ss.find("s", 7) == 7)
print(ss.find("s", 8) == 13)
print(ss.find("s", 8, 13 ) == -1)
print(ss.find(".") == len(ss)-1)

