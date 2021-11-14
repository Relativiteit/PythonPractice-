""" Assignment: electronics
    Created on 14-11-2021, 14:16
    @author Alejo Cain """
# Stating constant discount
DISCOUNT_PERCENTAGE = 0.15  # 15% discount
# naming variables and collecting user input
first = float(input("Enter the price of the first article: "))
second = float(input("Enter the price of the second article: "))
third = float(input("Enter the price of the third article: "))

# checking for largest number for first variable
if first > second and first > third:
    discount = first * DISCOUNT_PERCENTAGE
    total = (first + second + third) - discount
    print("The Discount:%.2f  with a Total: %.2f " %
          (discount, total))
# second is the largest number
elif second > third:
    discount2 = second * DISCOUNT_PERCENTAGE
    total2 = (first + second + third) - discount2
    print("The Discount: %.2f  with a Total: %.2f " %
          (discount2, total2))
# third is the largest number
else:
    discount3 = third * DISCOUNT_PERCENTAGE
    total3 = (first + second + third) - discount3
    print("The Discount: %.2f  with a Total: %.2f " %
          (discount3, total3))
