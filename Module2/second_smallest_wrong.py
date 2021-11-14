""" Assignment second_smallest
    Created on 14-11-2021,  14:28
    @author Alejo Cain """

# insertion sort from introduction to algorithms third edition
# I want to know the "normal way" to solve this problem with only using logic with while and for loops and not this given algorithmn
"""def insertionSort(number):

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
"""
a = input("Enter some numbers: ").split()
print(a)
smallest = a[0]
second_smallest = a[1]  # given a[1] is bigger then a[0]

for num in a:
    if num > smallest:
        second_smallest = smallest
        smallest = num
    elif num > second_smallest:  # this should only happen if the first if statement is not true
        second_smallest = num
print(smallest, second_smallest)
