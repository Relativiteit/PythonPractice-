"""while loops"""
# using while loops is good for when you don't know how many for loops you are going to need
# while loops are good for sorting a dictionary or list when you don't know how many elements

total2  = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0: # while givenlist value is higher than 0, and givenlist index is smaller then len givenlist
    total3 += given_list[i]
    i += 1
print(total3)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0: #if lement is smaller or 0 break out of this loop
        break
    total4 += element
print(total4)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0 # index
while True:
    total5 += given_list2[i]
    i += 1
    if given_list[i] <= 0: # when seeing a negative number break out of this loop
        break
print(total5)

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total7 = 0
j = 0
while j < len(given_list3):
    if given_list3[j] <= 0:
        total7 += given_list3[j]
        print(given_list3[j])
    j += 1
    print(total7)
print(len(given_list3))

given_list4 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total8 = 0
class Gutenburg:

    def you_mama():
        print("yo moma is so fat ")


for i in given_list4:
    if i < 0:
        total8 += i
        i += 1
        print(total8)

given_list5 = [5, 4, 4, 3, 1, -2, -3, -5]

total9 = 0
i = 0
while given_list5[i] > 0:
    total9 += given_list5[i]
    i += 1
print(total9)



