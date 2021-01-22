# classes contain function(methods) and data
class Ball(object):
    # __init__ is a special method called whenever you try to make
    # an instance of class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class
        self.position = (100, 100)
        self.velocity = (0, 0)

    # We can also add our own functions. When our ball bounces,
    # its vertical velocity will be negated. (no gravity here!)
    def bounce(self):
        self.velocity = (self.velocity[0], - self.velocity[1])
# superclass
class Room(object):
    # Note that we're taking an argument besides self, here.
    def __init__(self, name):
        self.name = name # Set the room's name to the name we got

# subclass taking
class WhiteRoom(Room): # A white room is a kind of room.
    def __init__(self):
        # All white rooms have names of 'White Room'.
    def interact(self, line):
        if 'test' in line:
            print "'Test'to you, too"
class RedRoom(Room):
    def __init__(self):
        self.name = 'Red Room'
    def interact(self, line):
        global current_room, white_room
        if 'white' in line:
            # We could create a new WhiteRoom, but then it
            # Would lose its data (if it had any) after moving
            # out of it and into it again.
            current_room = white_room
def main():
    reset_game()
    play_game()
if __name__ == '__main__': # If we're running as a script...
    main()
