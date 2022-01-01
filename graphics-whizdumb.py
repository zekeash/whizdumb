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
    t = Text(Point(1.0,p), '{}:1'.format(p+2))
    t.setFace("times roman")
    t.setStyle("bold")
    t.setTextColor("blue")    
    t.draw(win)
    r = Rectangle(Point(-2.5,-p+0.25),Point(2.5,-p-0.25))
    r.setFill('lightgreen')
    r.draw(win)
    t = Text(Point(1.0,-p), '{}:1'.format(p+2))
    t.setFace("times roman")
    t.setStyle("bold")
    t.setTextColor("blue")
    t.draw(win)

r = Rectangle(Point(-2.5,4),Point(2.5,4.5))
r.setFill('lightgreen')
r.draw(win)
t = Text(Point(1.0,4.25), '6:1\nAll answers are too high')
t.setFace("times roman")
t.setStyle("bold")
t.setTextColor("blue")
t.draw(win)

def placeAnswerCard(player,color,answer,pt,ll,ur):
    answerCard = Rectangle(ll,ur)
    answerCard.setFill(color)
    answerCard.draw(win)
    answerCardContents = Text(pt, '{}\n{}'.format(answer,player))
    answerCardContents.setFace("helvetica")
    answerCardContents.draw(win)

placeAnswerCard('Zeke', 'lightblue', '1999', Point(-0.75,1), Point(-1,0.8), Point(-0.5,1.2) )

placeAnswerCard('Rafi', 'orange', '2000', Point(-0.75,0), Point(-1,-0.2), Point(-0.5,+0.2) )

placeAnswerCard('Dad', 'red', '2001', Point(-0.75,-1), Point(-1,-0.8), Point(-0.5,-1.2) )

placeAnswerCard('Mom', 'blue', '2001', Point(-0.55,-1), Point(-0.8,-0.8), Point(-0.3,-1.2) )



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

