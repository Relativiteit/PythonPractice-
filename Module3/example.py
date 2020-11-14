NUMBER_OF_GRADES = 3

with open("C:\\Users\\PourChevre\\PycharmProjects\\VUPythonProject\\Module3\\grades.txt") as file:
    for line in file:
        line = line.replace('_', ' ').split()
        names, test_scores = line[:-NUMBER_OF_GRADES], line[-NUMBER_OF_GRADES:]
        name = ' '.join(names)  # Join names together.
        test_scores = [float(score) for score in test_scores]  # Make numeric.
        average_score = sum(test_scores) / len(test_scores)
        print('%s has an average grade of %.1f' % (name, average_score))