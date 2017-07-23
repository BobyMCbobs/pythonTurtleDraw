#import turtle and getch
from turtle import *
from msvcrt import getch

#start without the pen down
penup()

#predifined distance length
distance = 100

#2nd thing that assists with the pen being up
spaceup = True

#welcome message
print("Press space to put pen down, arrow keys to move")

#space bar function
def spaceBar(spaceup):
    if spaceup == True:
        spaceup = False
        pendown()
        print("Pen down")
        return spaceup
    
    elif spaceup == False:
        spaceup = True
        penup()
        print("Pen up")
        return spaceup

#always listening
while True:
    keytest = (ord(getch())) #listen to keys

    if keytest == 32: #spacebar
        spaceup = spaceBar(spaceup)
        
    # Arrow keys #
    if keytest == 75: #left arrow key
        left(90)
        print("Left")
        
    if keytest == 77: #right arrow key
        right(90)
        print("Right")

    if keytest == 72: #up arrow key
        forward(int(distance))
        print("Forward")

    if keytest == 80: #down arrow key
        backward(int(distance))
        print("Back")
