"""Assignment nuclear_power_plant
    Created on 08-11-2020, 08:10
    @author Alejo Cain """
# function to print a string multiple times
def warning_message(message, number_of_times):
    for i in range(number_of_times):
        print(message)
NUM_ITERATIONS = 3 #NEED TO DO THIS OR NO POINTS :(


"""Start program """

warning_message("NUCLEAR CORE UNSTABLE!!!\n"
                "Quarantine is in effect\n"
                "Surrounding hamlets will be evacuated\n"
                "Anti-radiationsuits and iodine pills are mandatory\n", NUM_ITERATIONS)


