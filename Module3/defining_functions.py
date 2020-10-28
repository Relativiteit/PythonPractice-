""" Assignment defining_functions
    Created on 27-10-2020
    @author Alejo Cain """

"""def repeat_print(message, number_of_times):
    #local variable x does not exist outside the function repeat_print() same for message and number of times
    #therefore you cannot print them outside of the function
    print(x)
    for i in range(number_of_times):
        print(message)
#global variable
x = 7
repeat_print("Hello goat", 5)
repeat_print("good stuff", 2)
"""
"""def repeat_print(message, number_of_times):
    #local variable x can be named the same as the global variable (shadowing)

    x = 8
    for i in range(number_of_times):
        print(message)
#global variable
x = 7
repeat_print("Hello goat", 5)
repeat_print("good stuff", 2)"""
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


#Good functions are reuable
#In general, functions hsould only be dependandt on their paraemters, and constants so local variables and such 