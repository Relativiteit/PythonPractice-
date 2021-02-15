import random

class CallCentre:

    def __init__(self):
        self.database = []
    def add(self, phone_number):
        self.database.append(phone_number)

    def give_phone_number(self):
        number_of_costumers = len(self.database)
        index = random.randint(0, number_of_costumers -1)
        return self = var = database[index]

    def remove (self, phone_number):
        self.database.remove(phone_number)

    def advertisement(self):
        print("advertisement")

    def call (self, phone_number):
        succes = 0
        result = random.randint(0,1)
        return result == SUCCESS
4
    def still_has_costumers(self):
        return self.database != []

# program

def read_costumers (name_database):
    result = CallCentre()
    file = open(name_database)
    input = file.read()
    phone_numbers = input.splitlines()
    for phone_number in phone_numbers
        result.add(phone_number)
        return result

call_centre = read_costumers("database")
while call_centre.still_has_customers()
    phone_number = call_centre.give_phone_number_customer()
    print("going to call: %s" % (phone_number))
    if call_centre.call(phone_number):
        call_centre.advertisement()
        call_centre.remove(phone_number)