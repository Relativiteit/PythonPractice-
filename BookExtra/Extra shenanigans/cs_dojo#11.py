""" Booleans """
type("microsoft")
type(4)
type(True)

a = 3
b = 1

if a > b:
    print("a is greater than b ")
if True:
    print("a is greater than b ")
boolean_value = a > b
#random
print(boolean_value)
if boolean_value:
    print("a is greater than b")
def are_you_sad(is_rainy, has_umbrella):
   return is_rainy and not has_umbrella
   # if is_rainy == True and has_umbrella == False:
   """if is_rainy and not has_umbrella: # same as above line but smaller 
        return True
    else:
        return False"""
""" The above block can be further simplified in code"""

are_you_sad(True, False)

def c_greater_thand_plus_e(c, d, e):
    return c > d + e
"""    if c > (d + e):
        return True
    else:
        return False
        """
print(c_greater_thand_plus_e(10, 2, 4))


