""" Assignment: vat
    Created on 23-10-2020
    @author Alejo Cain """
#Assignment finding the price
VAT = 1.21 #updated on 23-10-2020

#input of price with tax
price_with_tax = float(input("Enter the price of an article including VAT: " ))
#calculation of price
price = price_with_tax / VAT
#output, first price without VAT and then without, using %.2f notation for ease of reading
print("This article will cost %.2f euro without 21.00%% VAT and %.2f with VAT " \
        % (price, price_with_tax))