"""for loops"""

a = ["banana", "apple", "microsoft"]

for element in a:
    print(element)

b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
print(total)

# 1 , 2, 3, 4

c = list(range(1, 5))

print(c)

for i in range(1,5):
    print(i)
total2 = 0
for i in range(1, 5):
    total2 += i
print(total2)

print(list(range(1, 8 )))

total3 = 0
for i in range(1,8):
    if i % 3 == 0 :
        total3 += i
print(total3)

print(list(range(1, 100)))
total4 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total4 += i
print(total4)
