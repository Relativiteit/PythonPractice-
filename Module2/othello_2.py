""" Assignment othello_2
    Created on 14-11-2021, 14:19
    @author Alejo Cain """
# input of time for human time and computer time
black_player = int(
    input("Enter the time the black player thought in milliseconds: "))
white_player = int(
    input("Enter the time the white player thought in milliseconds: "))

# there has to be a way to do this piece of code only one time?
# Calculation of time
hours = (black_player/(1000*60*60)) % 24
minutes = (black_player/(1000*60)) % 60
seconds = (black_player/1000) % 60

hours2 = (white_player/(1000*60*60)) % 24
minutes2 = (white_player/(1000*60)) % 60
seconds2 = (white_player/1000) % 60

if black_player > white_player:
    print("The time the human player uses black pieces has spent thinking is: %02d:%02d:%d" % (
        hours, minutes, seconds))
else:
    print("The time the human player using white pieces has spent thinking is: %02d:%02d:%d" % (
        hours2, minutes2, seconds2))
