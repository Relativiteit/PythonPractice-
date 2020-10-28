''' Assignment: mile_in_kilometer
    Created on 23-10-2020
    @author: Alejo Cain '''
#define conversion rate
MILE_IN_KILOMETERS = 1.609344
#Gather input from user
number_of_miles = int(input("Enter the number of miles: "))
#calculation
numbers_of_kilometers = number_of_miles * MILE_IN_KILOMETERS
#use \ to split this line to make it shorter and use %.2f to get 2 decimals
#output
print("%.2f miles equals %.2f kilometer" %\
      (number_of_miles, numbers_of_kilometers))
