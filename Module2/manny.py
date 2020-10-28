""" Assignment manny
    Created on 25-10-2020, 13:14
    @author Alejo Cain """
#Input of donation needed
donation = int(input("How much do you want to donate to the charity Thirsty toads in the Sahara Aka: "))
#While statement to check if donation is higher then 50
while donation - 50 < 0:
    print("Can you please reconsider your donation of %d and look into your heart " % donation)
    break
else:
    print("Because of your %d euro many thirsty toads can now drink in the great sandy plains" % donation)
# this works now lets try to do this a bit more realistic

"""#Same program but with added error exception
while True:
    try:
        #input of donation
        donation = float(input("How much do you want to donate to the charity Thirsty toads in the Sahara Aka: "))
    except ValueError: #require user to enter a number instead of letters
        print("Please enter a number, try again. ")
        #go back to the beginning of the loop
        continue
    else:
        #value was a integer no need for loop
        break
#Checking of donation is high enough to pass 
while donation - 50 < 0:
    print("Can you please reconsider your donation of %.2f EURO and look into your heart " % donation)
    break
else:
    print("Because of your %.2f EURO many thirsty toads can now drink in the great sandy plains" % donation)""""



