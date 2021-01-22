""" List comprehension basics """

a =[1, 3, 5, 7, 9, 11]
# =[2, 6, 10, 14, 18, 22] double of value
# .append
b = []
b.append(10)
b.append(20)

print(b)

c = []
for i in a:
    c.append(i * 2)
print(c)

""" list comprehension """
d = [i * 2 for i in a ]
print(d)

# [1, 4, 9, 16, 25, 36]
e = [i ** 2 for i in range(1, 7)]
print(e)

el = []
for i in range(1, 7):
    el.append(i ** 2)
print(el)

# [36, 25, 16, 9, 4, 1]
back = []
for i in range(6, 0, -1):
    back.append(i ** 2)
print(back)
"""" list comprehension style """
becky = [i ** 2 for i in range(6, 0, -1)]
print(becky)


