""" Assignment count_house_number
    Created on 17-11-2020, 19:42
    @author Alejo Cain """
def read_house_number(address):
    address = address.split(";")
    house_number = int(address[1])
    return house_number


def has_house_number(student, house_number):
    student = student.split("-")
#    name = student[0] don't need name for now
    address = student[1]
    return read_house_number(address) == house_number


def count_house_number(school, house_number):
    students = school.splitlines()
    result = 0

    for student in students:
        if has_house_number(student, house_number):
            result += 1 # local variable
    return result

schools = open("C:/Users/PourChevre/PycharmProjects/VUPythonProject/Module4/input")
result = 0 # global variable
for school in schools:
    result += count_house_number(school, 3 )
print(result)

