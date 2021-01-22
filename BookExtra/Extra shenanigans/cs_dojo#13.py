""" sets, a set is an unordered collection with no duplicate elements,
Basic uses include membership testing and eliminating testing and eliminating duplicate entries
 Set objects also support mathematical operations like union, intersection, difference and symmetric difference"""

a = set()
print(a)

""" adding elements to the set """
a.add(1)
print(a)

a.add(2)
print(a)

for i in a:
    print(i)

""" Taking out duplicates from a list """
given_list1 = [1, 1, 2, 4, 2]
new_set1 = set()
for i in given_list1:
    new_set1.add(i)
print(new_set1) # {1, 2, 4} no more duplicates


new_list1 = list()
for i in new_set1:
    new_list1.append(i)
print(new_list1)

b = set()
b.add('apple')
b.add('banana')
b.add(1)
print(b)

given_list2 = [1, 3, 4, 1, 3]
new_list2 = sum(set(given_list2))
print(new_list2)

""" explicit way """
new_set2 = set()
for i in given_list2:
    new_set2.add(i)
total = 0
for i in new_set2:
    total += i
print(total)


