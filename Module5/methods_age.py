class AgeRow(object):

    def __init__(self):
        self.age_row = []

    def add(self, age):
        self.age_row.append(age)

    def number_in_range(self, start, send):
        # Calculates how many passengers are in the range
        # bounded by start and end
        result = 0

        for age in self.age_row:
            if start <= age and age <= end:
                result += 1
        return result

import sys
from age_row import AgeRow
""" Assignment: Airplane 
    Created on 03-12-2020
    @author: Alejo Cain """

MAX_TODDLER_AGE= 4 # year
MAX_CHILD_AGE = 12 # ""
MAX_ADULT_AGE = 64 # ""
MAX_AGE = 135      # ""

ADULT_FARE = 99.0 # euro
TODDLER_FARE = ADULT_FARE * 0.1
CHILD_FARE = ADULT_FARE * 0.5
ELDERLY_FARE = ADULT_FARE *1.1

def read_in_range(input_string, start, end) :
    result = int(input_string)

    if result < start or result > end :
        print("ERROR: %d is not in range (%d, %d)" % (result, start, end))
        sys.exit(1)
    return result

def read_age(input_string) :
    return read_in_range(input_string, 0, MAX_AGE)

def read_age_row(passengers):
    result = AgeRow()

    for passenger in passengers :
        age = int(passenger)
        result.add(age)

    return result

def calculate_profit(start, end, fare, ageRow):
    return ageRow.number_in_range(start, end) * fare

def calculate_total_profit(max_toddler_age, age_row):
    toddler_profit = calculate_profit(0, max_toddler_age, TODDLER_FARE, age_row)

    children_profit = calculate_profit(max_toddler_age + 1, \
                    MAX_ADULT_AGE, ADULT_FARE, age_row)
    elderly_profit = calculate_profit(MAX_ADULT_AGE + 1, \
                                      MAX_AGE, ELDERLY_FARE, age_row)
    return toddler_profit + children_profit + \
            adult_profit + elderly_profit
def print_change_in_profit(old_profit, new_profit):
    print("When using the new age limits for " + \
          "toddleres and children \n the profit " + \
          "changes from EUR %8.2f to EUR %.2f. "% \
          (old_profit, new_profit))
    print("The difference is EUR %8.2f."%\
          (new_profit - old_profit))

''' Start Program '''

file = open("input.txt")
passengers = file.readline().split()
ages = file.readline()
age_row = read_age_row(passengers)
new_max_toddler_age = read_age(ages)

normal_profit = calculate_total_profit(MAX_TODDLER_AGE, age_row)
new_profit = calculate_total_profit(new_max_toddler_age, age_row)

print_change_in_profit(normal_profit, new_profit)


