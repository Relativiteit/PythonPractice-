import random

class CallCentre:

    def __init__ (self):
        self.database = []

    def add (self, phone_number):
        self.database.append(phone_number)

    def still_has_customers (self):
        return len(self.database) != 0

    def give_phone_number_customer (self):
        number_of_customers = len(self.database)
        index = random.randint(0, number_of_customers-1)
        return self.database[index]

    def call (self, phone_number):
        SUCCESS = 0
        result = random.randint(0, 1)
        return result == SUCCESS

    def advertisement(self):
        print('advertisement')

    def remove(self, phone_number):
        self.database.remove(phone_number)











#program

def read_customers (name_database):
    result = CallCentre()
    file = open(name_database)
    input = file.read()
    phone_numbers = input.splitlines()
    for phone_number in phone_numbers:
        result.add(phone_number)
    return result

call_centre = read_customers('database')
while call_centre.still_has_customers():
    phone_number = call_centre.give_phone_number_customer()
    print 'going to call: %s' % (phone_number)
    if call_centre.call(phone_number):
        call_centre.advertisement()
        call_centre.remove(phone_number)

