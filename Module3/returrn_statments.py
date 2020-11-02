""" Assignment return_statement
    Created on 27-10-2020,  09:54
    @Author Alejo CAin """

"""def round(n):
    return int(n + 0.5)

#print(round(1.5)+ 5)
print(round(1.51))"""
# Program returning the number of vowels from user input
VOWELS = ["A","E", "I", "O", "U", "a", "e", "i", "o", "u"]

def count_vowels(text):
    number_of_vowels = 0
    for charecter in text:
        if charecter in VOWELS:
            number_of_vowels += 1
    return number_of_vowels

#assign count_vowels to a variable
x = count_vowels("Hello world")
#print how many vowels
print(x)

print(count_vowels("That is amazing"))