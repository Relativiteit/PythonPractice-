""" Assignment: electronics_battered
    Created on 24-10-2020, 08:01
    @author Alejo Cain """
#Stating constant discount
DISCOOUNT_PERCENTAGE = 0.15 #15% discount
#naming variables and collecting user input
first = float(input("Enter the price of the first article: "))
second = float(input("Enter the price of the second article: "))
third = float(input("Enter the price of the third article: "))

#checking for largest number for first variable
if first > second and first > third:
    discount = first * DISCOOUNT_PERCENTAGE
    total = (first + second + third) - discount
    print("The discount will be %.2f EURO with a total of %.2f EURO" % (discount,total))
#second is the largest number
elif second > third:
    discount2 = second * DISCOOUNT_PERCENTAGE
    total2 = (first + second + third) - discount2
    print("The discount will be %.2f EURO with a total of %.2f EURO" % (discount2, total2))
#third is the largest number
else:
    discount3 = third * DISCOOUNT_PERCENTAGE
    total3 = (first + second + third) - discount3
    print("The discount will be %.2f EURO with a total of %.2f EURO" % (discount3, total3))
