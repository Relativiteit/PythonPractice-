"""Assignment nuclear_power_plant
    Created on 08-11-2020, 10:15
    @author Alejo Cain """

def warning_message(message, number_of_times):
    for i in range(number_of_times):
        print(message)


"""Start program """

warning_message("NUCLEAR CORE UNSTABLE!!!\n"
                "Quarantine is in effect\n"
                "Surrounding hamlets will be evacuated\n"
                "Anti-radiationsuits and iodine pills are mandatory\n", 3)


