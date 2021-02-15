""" events
    Created on 15/02/2021 09:00
    @author Alejo Cian """

from ipy_lib import SnakeUserInterface

WIDTH = 9
HEIGHT = 9

def process_event(event):
    if event.name == "arrow":
        print("hello")
    print("%s - %s" % (event.name, event.data))



ui = SnakeUserInterface(WIDTH, HEIGHT)
ui.set_animation_speed(2)

while True:
    event = ui.get_event()
    process_event(event)

