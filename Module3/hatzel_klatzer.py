import sys

""" Assignment hatzel_klatzer
    Created on 02-11-2020, 09:12
    @author: Alejo Cain """

STARTING_YEAR = 1950
FINAL_YEAR = 2050
def print_percentage_of_cases(percentage):
    print("The percentage of illness that match" +\
            "the hypothesis is: %.2f" % percentage)

    # Reads a number from the input string. If the number is not
    # In range the program will print an error message and
    # Terminates. Otherwise, the number is returned.
def read_in_range(input_string, start, end):
    result = int(input_string)
    if result < start or result > end:
        print("ERROR: %d is not in range( %d, %d)" % \
              (result, start, end))
        sys.exit(1)
    return result

def odd_month(input_string):
    date = input_string.split()

    # The day is read, but not seaved
    read_in_range(date[0], 1, 31)

    # The month is read and saved in the variable "month"
    month = read_in_range(date[1], 1, 12)

    # The year is read, but not saved
    read_in_range(date[2], STARTING_YEAR, FINAL_YEAR)

    return month % 2 != 0

"""Start Program"""
total_number_of_seizures = 0
number_in_odd_months = 0

lines = open("C:/Users/PourChevre/PycharmProjects/PythonVU/VUPythonProject/Module3/input.txt").readlines()
for line in lines:
    if odd_month(line): #if odd months is found in the text file add 1 to numer in odd months and total number of seizures
        number_in_odd_months += 1

    total_number_of_seizures += 1

percentage = (float(number_in_odd_months) /
              total_number_of_seizures) * 100.0

print_percentage_of_cases(percentage)


