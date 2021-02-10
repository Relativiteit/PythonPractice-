""" chapter 7 extra practise
    created on 04/02/2021
    @author Alejo Cain """

def seq3np1(n):
    """ print the 3n+1 sequence from n, terminating when it reaches 1."""

    while n!= 1:
        print(n, end=",") # end="," makes the output run on one line
        if n % 2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
    print(n, end=".\n")
print(seq3np1(40))
