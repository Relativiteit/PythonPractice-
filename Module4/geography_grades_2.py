""" Assignment geography_grades_2
    Created on 18-11-2020, 10:23
    @author Alejo Cain """


def has_test_score(student, test_score):
    student = students.split("_")
    name = student[0]
    grade1 = student[1]
    grade2 = student[2]
    grade3 = student[3]
    return read_test_score(grade1, grade2, grade3,) == total_test_score
    return read_test_score(name)


def count_test_score(grades, test_score):
    students = grades.splitlines()
    result = 0

    for student in students:
        if has_test_score(student, test_score)
            result += 1
    return result



grades = open("C:/Users/PourChevre/PycharmProjects/VUPythonProject/Module4/input")
result = 0
for grade in grades:
    result += count_test_score(grade, 3)
