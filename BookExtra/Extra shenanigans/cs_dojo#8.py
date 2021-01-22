"""" Dictionary """
""" Look up table """
d = {} # d = dict() is the same thing
        #key    value
# d = {"George": 24, "Tom": 32}
""" Adding new elements to dictionary """
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

""" finding values of the keys """
print(d["George"])
print(d["Tom"])

""" Assigning new values """
d["Jenny"] = 20
print(d["Jenny"])

# keys are commonly strings or numbers

d[10] = 100
print(d[10])

""" How to iterate over key-value pairs """
# key is just a variable just as value, these can be changed to anything
for key, value in d.items():
    print("Key:", key)
    print("Value:", value)
    print("\n")

