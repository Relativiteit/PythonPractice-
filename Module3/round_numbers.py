"""def round(n):
    return int(n+ 0.5)

print(round(1.5) + 5)
print(round(1.49))
"""

VOWELS = ["A","E","I","O", "U", "a", "e", "i", "o", "u"]


def count_vowels(text):
    number_of_vowels = 0
    for character in text:
        if character in VOWELS:
            number_of_vowels += 1

    return number_of_vowels

print(count_vowels("Hellow world"))

x = count_vowels("Hellow worlds steam boats ")

print(x)


