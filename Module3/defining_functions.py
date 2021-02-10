""" Assignment defining_functions
    Created on 27-10-2020
    @author Alejo Cain """


#def change(parameter)
def change(x):
    #modifying value of parameter
    x = 5
    print(x)
#global variable
x = 6
#calling change updates the value to 6 change(argument)
change(x)
print(x)


#Good functions are reusable
#In general, functions should only be dependant on their parameters, and local variables.