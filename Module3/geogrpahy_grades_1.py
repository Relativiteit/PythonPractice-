""" Assignment geography_grades_1
    Created on 14-11-2020, 20:12
    @author Alejo Cain """

def convert_line_to_grades(line):
    name = ""
    checking_name = True
    score_text = ""
    for letter in line:
        if letter != "_" and checking_name:
            name += letter
        if letter == "_" and checking_name:
            checking_name = False
        if letter != "_" and not checking_name:
            score_text += letter

    score_text = score_text.split(" ")
    score_value = []
    for score in score_text:
        if(score == ''):
            continue
        score_value.append(float(score))

    return (name, score_value)

def average_grade(grades):
    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    return average

# main
text = open("grades.txt").read().split("\n")
for line in text:
    name, score_value = convert_line_to_grades(line)
    if(len(score_value) == 0):
        continue
    average = average_grade(score_value)
    print(str(name) + " %.2f" % average)



