""" Assignment second_smallest
    Created on 27-10-2020,  08:36
    @author ALejo Cain """

#insertion sort from introduction to algorithms third edition
#i want to know the "normal way" to solve this problem with only using logic with while and for loops and not this given algorithmn
def insertionSort(number):

    for i in range(1, len(number)):

        key = number[i]

        j = i - 1
        while j >= 0 and key < number[j]:
            number[j + 1] = number[j]
            j -= 1
        number[j + 1] = key


number = input("Enter some numbers: ").split()
insertionSort(number)
for i in range(len(number)):
    print(number[i])
print(number[1])
#need help SOS hahaha