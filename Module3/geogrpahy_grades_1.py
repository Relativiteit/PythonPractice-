""" Assignment geography_grades_1
    Created on 14-11-2020, 20:12
    @author Alejo Cain """

def convert_text_to_grades(text):
    names = []
    scores = []
    for line in text:
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

        scores.append(score_value) # list(scores) with lists of grades(score_value)
        names.append(name)
    return (scores, names)

def average_grade(grades):
    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    return average

# main
text = open("grades.txt").read().split("\n")
scores, names = convert_text_to_grades(text)

# print
for i, score in enumerate(scores):
    if(len(score) == 0):
        continue

    average = average_grade(score)
    print(str(names[i]) + " %.2f" % average)