""" lists """

a = [3, 10, -1]
a.append(1)
a.append("hello")
a.append([1,2]) # you can append
a.pop() # take out the last element of the list [1,2]
a.pop() # take out the last element of the list "hello"
print(a)

print(a[0])
a[0] = 100
print(a[0])

b = ["banana", "apple", "microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
# this can also be done with the following statement on line 22
c = ["banana", "apple", "microsoft"]

c[0], c[2] = c[2], c[0]
print(c)



