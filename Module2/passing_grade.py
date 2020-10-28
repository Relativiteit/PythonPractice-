""" Assignment: passing_grade
    Created on 24-10-2020, 07:32
    @author Alejo Cain """

PASS_MINIMUM = 5.5
grade = float(input("Enter a grade: "))

if grade >= PASS_MINIMUM:
    print("The grade, %0.2f, is a pass." % grade)
else:
    print("The grade %0.2f , is not a pass" % grade)

#names of variables, methods and functions are written number_of_students
#identifiers of constants are written MAXIMUM_NUMBER_OF_STUDENTS
#identifiers of modules are written types_of_courses
#identifiers for classes are written lowercase with capital first letter Gym, Library, Farm

