""" Chapter 7 extra practise
    Created on 08:02
    @author Alejo Cain """
def print_any_mult_table(high):
    for i in range (1, high+1):
        print_multiples(i)

def print_mult_table():
    for i in range(1, 7):
        print(print_multiples(i))

def print_multiples(n):
    for i in range(1,7):
        print(n * i, end="   ")
    print()
# print_multiple(1) # 1   2   3   4   5   6

#for i in range(1,7):
 #   print_multiple(i) # output multiplication table
""" 1   2   3   4   5   6   
    2   4   6   8   10   12   
    3   6   9   12   15   18   
    4   8   12   16   20   24   
    5   10   15   20   25   30   
    6   12   18   24   30   36   """
print(print_mult_table())
print(print_any_mult_table(7))

