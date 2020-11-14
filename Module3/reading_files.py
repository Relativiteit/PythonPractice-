""" Assignment read_files
    Created on 14-11-2020, 20:41
    @author Alejo Cain """


def sum_numbers(line):
    numbers = line.split()
    result = 0

    for number in numbers:
        result += int(number)
    return result


file = open("C:/Users/PourChevre/PycharmProjects/PythonVU/VUPythonProject/Module3/input.txt").read()
lines = file.splitlines()

for line in lines:
    print(sum_numbers(line))
# .strip() function removes trailing or leading spaces in a string