""" lists_loops
    Created on 10/02/2021
    @author ALejo Cain """
xs = [1, 2, 3, 4, 5]

for i in range(len(xs)):
    xs[i] = xs[i]**2 # squared
    print(xs[i])

""" enumerate """

xd = [1, 2, 3, 4, 5]
for (i, val) in enumerate(xd):
    xd[i] = val**2
    print(xd[i])
""" enumerate fruit """

for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
    print(i, v)
    