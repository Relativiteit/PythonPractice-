"""" Assignment alphabet
    Created on 25-10-2020, 19:30
    @author Alejo Cain """
""""#Get input from user
sentence = input("Enter some text please: ")
number_of_times = int(input("Enter the number of times: "))
#The range function has 3 arguments (start, stop, increments)
for i in range(number_of_times): #if you only use 1 argument it will take start as 0 and incrments +1
    print(sentence) 

result = ''
for i in range(ord('0'), ord('9') + 1):
    c = chr(i)
    result = result + c
    print(result) #put the print function here to see every addition during every loop
print(result) # or put print here to just get the numbers in 1 row """
#make empty string
alphabet = ''
#set start 0 stop 26 third argument empty makes it 1
for i in range(0, 26,):
    #+= adds to the number already in the variable >> in this case + 1 so gaining one step in alphabet
    alphabet += chr(ord("a")+ i)
#show string outside the loop to get it on 1 line.
print(alphabet)

