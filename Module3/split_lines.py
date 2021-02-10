""" Module 3 extra practise """

def sum_numbers(line):
    numbers = line.split()
    result = 0
    for number in numbers:
        result += int(number)
    return result

file = open("input.txt").read()
lines = file.splitlines()

for line in lines:
    print(sum_numbers(line), end=",")
