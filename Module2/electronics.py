""" Assignment: electronics
    Created on 14-11-2021, 15:33
    @author Alejo Cain """
# Stating constant discount
DISCOUNT_PERCENTAGE = 0.15  # 15% discount
# naming variables and collecting user input
first = float(input(""))
second = float(input(""))
third = float(input(""))

# checking for largest number for first variable
if first > second and first > third:
    discount = first * DISCOUNT_PERCENTAGE
    total = (first + second + third) - discount
    print("Discount:%.2f" %
          (discount))
    print("Total:%.2f" % (total))
# second is the largest number
elif second > third:
    discount2 = second * DISCOUNT_PERCENTAGE
    total2 = (first + second + third) - discount2
    print("Discount:%.2f" %
          (discount2))
    print("Total:%.2f" % (total2))
# third is the largest number
else:
    discount3 = third * DISCOUNT_PERCENTAGE
    total3 = (first + second + third) - discount3
    print("Discount:%.2f" %
          (discount3))
    print("Total:%.2f" % (total3))
