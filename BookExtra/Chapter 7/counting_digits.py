""" chapter 7.7 counting digits"""

def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(710))

def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

print((num_zero_and_five_digits(1055030250) == 7))
print(num_digits(0))
