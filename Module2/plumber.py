''' Assignment: plumber
    Created on 14-11-2021
    @author Alejo Cain     '''

# Plumbing law basic rate for call out, constant
CALL_OUT = 16.00
# hourly wage to be entered by user
hourly_wage = float(input("Enter hourly wages: "))
# hours worked to be entered by user
hours_worked = float(input("Enter the number of hours worked: "))
# round the float to the closest integer, rounds down until .5 including .5 so be wary!!
hours_billable = round(hours_worked + 0.5)
# calculation of total cost
total_cost = (hourly_wage * hours_billable) + CALL_OUT

print("The total cost will be %.2f euro consisting of %.1f hours billed at %.2f euro rate"
      % (total_cost, hours_worked, hourly_wage))
