""" Chapter 4 practise
    Created on 04-02-2021
    @author Alejo Cain """

def final_amt(p, r, n , t):
    """ Apply the compound interest formula to p to produce the final amount."""


    a = p * (1+ r/n) ** (n*t)
    return a        # This is new, and makes the function fruitful
# now that we have the function above, Let us call it
toInvest = float(input("how much do you want to invest? "))
fnl = final_amt(toInvest, 0.08, 12, 5) # 8% interest compounded 12 times for 5 years
print("At te end of the period you'll have ", fnl)
