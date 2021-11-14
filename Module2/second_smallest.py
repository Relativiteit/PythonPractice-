""" Assignment second_smallest
    Created on 14-11-2021, 15:15
    @author ALejo Cain """
""" Take a unknown number of positive integers as input. Assume that the first
number is always smaller than the second, all numbers are unique and the input consists of a least three
integers. Print the second smallest integer"""
# trying to use insertion sort the manual is vague on how to go from splitting simple list to solving this question
# aka no idea how to do it but this without sort so i made a sorting algorithm XD


def insertionSort(numbers):
    for j in range(1, len(numbers)):
        key = numbers[j]
        i = j - 1
        while i > 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i = i - 1
        numbers[i+1] = key


numbers = input("Enter some numbers: ").split()
print(numbers)
insertionSort(numbers)
print(numbers)

for i in range(len(numbers)):
    print(numbers[i])
