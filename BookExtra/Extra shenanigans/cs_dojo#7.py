"""more for loops """

total = 0
for i in range(1, 5):
    total += i
print(total)
print("\n")

a = ["apple", "banana", "republic"]

for element in a:
    print(element)
print("\n")
for i in range(0, 3):
    print(i)
print("\n")
for i in range(3):
    print(i)
print("\n")
for i in range(3):
    print(a[i])
print("\n")
for i in range(len(a)):
    print(a[i])
print("\n")

for i in range(len(a)):
    for j in range(i + 1):
        # i = 0 -> j = 0
        # i = 1 -> j = 0, 1
        # i = 2 -> j = 0, 1, 2
        print(a[i])
print("\n")

print(list(range(1, 100)))
total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)

total2 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 ==0 :
        total2 += i
print(total2)
# tutorial 6
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total3 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total3 += given_list[j]
    j -=1
print(total3)




