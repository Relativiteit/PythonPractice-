""" count_house_number_extra
    Created on 10/02/2021
    @author ALejo Cain """
def read_house_number(address):
    address = address.split(";")
    house_number = int(address[1])
    return house_number

def has_house_number(student, house_number):
    student = student.split("-")
    # name = student[0] dont need it right now but good to know
    address = student[1]
    return read_house_number(address) == house_number

def count_house_number(school, house_number):
    students = school.splitlines()
    result = 0

    for student in students:
        if has_house_number(student, house_number): # has boolean function
            result += 1

    return result


schools = open("input").read().split("=")
result = 0


for school in schools:
    result += count_house_number(school, 3)

print(result)

