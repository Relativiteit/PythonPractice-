"""" Assignment alphabet
    Created on 14-11-2021, 14:25
    @author Alejo Cain """

# make empty string
alphabet = ''
# set start 0 stop 26 third argument empty makes it 1
for i in range(0, 26,):
    # += adds to the number already in the variable >> in this case + 1 so gaining one step in alphabet
    alphabet += chr(ord("a") + i)
# show string outside the loop to get it on 1 line.
print(alphabet)
