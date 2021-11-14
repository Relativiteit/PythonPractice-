""" Assignment manny
    Created on 14-11-2021, 14:20
    @author Alejo Cain """
# Input of donation needed
a = []
donation = int(input(
    "How much do you want to donate to the charity Thirsty toads in the Sahara Aka: "))
print(donation)

while ((donation - 50) < 0):
    print("Can you please reconsider your donation of %.2f and look into your heart " % donation)

    donation = int(input(
        "How much do you want to donate to the charity Thirsty toads in the Sahara Aka: "))

    print(donation)

else:
    print("Because of your %.2f euro many thirsty toads can now drink in the great sandy plains" % donation)
