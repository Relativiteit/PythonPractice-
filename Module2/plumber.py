''' Assignment: plumber
    Created on 23-10-2020
    @author Alejo Cain     '''
#Assignment background story THE MAVERICK MONKEY
'''the hourly wages multiplied by the number of billable hours plus the callout cost. 
The number of billable hours is the number of hours worked rounded
to the nearest integer. Plumbing laws fix the call-out cost at e16,00.'''

#Plumbing law basic rate for call out, constant
CALL_OUT = 16.00
#hourly wage to be entered by user
hourly_wage = float(input("Enter hourly wages: "))
#hours worked to be entered by user
hours_worked = float(input("Enter the number of hours worked: "))
#round the float to the closest integer, rounds down untill .5 including .5 so be wary!!
hours_billable = round(hours_worked)
#calculation of total cost
total_cost = (hourly_wage * hours_billable) + CALL_OUT

print("The total cost will be %.2f euro consisting of %.0f hours billed at %.2f euro rate" \
      % (total_cost, hours_billable, hourly_wage))




