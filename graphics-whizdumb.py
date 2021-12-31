# https://www.cs.swarthmore.edu/~adanner/cs21/s15/Labs/graphics.php

import numpy as np
from tkinter import *
from graphics import *


## Create a 1000 pixel x 1000 pixel graphics window
win = GraphWin("Whizdumb Playing Board", 1000, 1000,autoflush=False)
## Give it a green background
win.setBackground("darkgreen")

## Give window coordinates
win.setCoords(-5, -5, 5, 5)

for p in range(4):
    r = Rectangle(Point(-2.5,p+0.25),Point(2.5,p-0.25))
    r.setFill('lightgreen')
    r.draw(win)
    t = Text(Point(0,p), '{}:1'.format(p+2))
    t.setFace("times roman")
    t.setStyle("bold")
    t.setTextColor("blue")    
    t.draw(win)
    r = Rectangle(Point(-2.5,-p+0.25),Point(2.5,-p-0.25))
    r.setFill('lightgreen')
    r.draw(win)
    t = Text(Point(0,-p), '{}:1'.format(p+2))
    t.setFace("times roman")
    t.setStyle("bold")
    t.setTextColor("blue")
    t.draw(win)

r = Rectangle(Point(-2.5,4),Point(2.5,4.5))
r.setFill('lightgreen')
r.draw(win)
t = Text(Point(0,4.25), '6:1\nAll answers are too high')
t.setFace("times roman")
t.setStyle("bold")
t.setTextColor("blue")
t.draw(win)
    
answerCard = Rectangle(Point(-1,0.8),Point(-.5,1.2))
answerCard.setFill('lightblue')
answerCard.draw(win)
answerCardContents = Text(Point(-.75,1) , '1999\nZeke')
answerCardContents.draw(win)

answerCard = Rectangle(Point(-1,-0.2),Point(-.5,+0.2))
answerCard.setFill('orange')
answerCard.draw(win)
answerCardContents = Text(Point(-.75,0) , '2000\nRafi')
answerCardContents.draw(win)


answerCard = Rectangle(Point(-1,-0.8),Point(-.5,-1.2))
answerCard.setFill('red')
answerCard.draw(win)
answerCardContents = Text(Point(-.75,-1) , '2004\nDad')
answerCardContents.draw(win)

chip = Circle(Point(-1.75,1), 0.15)
chip.setFill('lightblue')
chip.draw(win)
chipValue = Text(Point(-1.75,1), '2')
chipValue.draw(win)

chip = Circle(Point(-1.75,0), 0.15)
chip.setFill('orange')
chip.draw(win)
chipValue = Text(Point(-1.75,0), '1')
chipValue.draw(win)

chip = Circle(Point(-1.55,1), 0.15)
chip.setFill('orange')
chip.draw(win)
chipValue = Text(Point(-1.55,1), '1')
chipValue.draw(win)



chip = Circle(Point(-1.75,4.25), 0.15)
chip.setFill('red')
chip.draw(win)
chipValue = Text(Point(-1.75,4.25), '2')
chipValue.draw(win)


