""" Assignment geography_grades_1
    Created on 14-11-2020, 20:12
    @author Alejo Cain """



grades = open("C:\\Users\\a.cain\\PycharmProjects\\VUPythonProject\\Module3\\grades.txt").read()
school = grades.split("_")
result = 0 # global variable
"""for grade in grades:
    result += count_test_score(grade, 3) """
print(type(grades))
