""" Assignment geography_grades_1
    Created on 14-11-2020, 20:12
    @author Alejo Cain """
# constant value
RECIEVED_GRADES = 3
# reading file from hard drive
file = open("C:\\Users\\PourChevre\\PycharmProjects\\VUPythonProject\\Module3\\grades.txt")
def average_grade():
    for grade in file:
        # skipping underscores
        grade = grade.replace("_", " ").split()

        students, exam_results = grade[:-RECIEVED_GRADES], grade[-RECIEVED_GRADES:]
        # appending names
        student = " ".join(students)
        #
        exam_results = [float(score) for score in exam_results]
        #calculating average
        average_score = sum(exam_results) / len(exam_results)
        # trying to use f strings instead of %.2f .... % student, method
        print(f"{student} has a average exam result of {average_score:.1f}")

    return

print(average_grade())



"""
print(file[0])
print(file[1])
print(file[2])
print(file[3]) """


#print(file)