class Robot:
    def __init__(self, Name, Color, Weight):
        self.name = Name
        self.color = Color
        self.weight = Weight
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)
r1.introduce_self()
r2.introduce_self()



class Person:
    def __init__(self, Name, Personality, isSitting):
        self.name = Name
        self.personality = Personality
        self.is_sitting = isSitting
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
    def extra_info(self):
        print("Hello my name is " + self.name + " people see me as " + self.personality)

p1 = Person("Alice","aggresive", False)
p2 = Person("Becky", "talkative", True)

""" How to add new features, """
p1.robot_owned = r2
p2.robot_owned = r1
# not possible to take the methods from Person class and Robot class in one statement
p1.extra_info()
p1.robot_owned.introduce_self()



