#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.constants import *
from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
import random

ct = [ ["Leg!", "+1d4", "Slowed", "Until end of target's turn", "Save ends", "Save ends", "Until end of encounter"],
       ["Arm!", "+1d4", "Weakened", "Until end of your turn", "Save ends", "Save ends (DC12)", "Until end of encounter"],
       ["Wound!", "+1d4", "Ongoing damage", "Save ends (DC1d4+2)", "Save ends (DC1d6+2)", "Save ends (DC1d8+2)", "Save ends (DC1d10+2)"],
       ["Large wound!", "+1d6", "Ongoing damage", "Save ends (DC1d6+2)", "Save ends (DC2d4+2)", "Save ends (DC1d10+2)", "Save ends (DC2d6+2)"],
       ["Head!", "+1d6", "Dazed", "Until end of target's next turn", "Save ends", "Save ends", "Until end of encounter"],
       ["Knockdown", "+1d8", "Prone"],
       ["Face!", "+1d8", "Blinded", "Until end of your next turn", "Until end of target's next turn", "Save ends", "Save ends (DC12)"],
       ["Eyes!", "+2d4", "-2 attack penalty", "Until end of target's next turn", "Until end of target's next turn", "Save ends", "Save ends"],
       ["Resolve!", "+2d6", "-2 all defenses", "Until start of target's next turn", "Until start of your next turn", "Save ends", "Save ends (DC12)"],
       ["Brain!", "+4d4", "Stunned", "Until end of your next turn", "Save ends", "Save ends", "Until end of encounter"],
       ["EPIC!", "+3d8", "Unconsious for 1d4 rounds"] ]

class Table:        
    def __init__(self):
        w = Toplevel()
        w.title('Critical Hit Table')
        w.geometry('+150+150')
        frame = Frame(w)
        frame.grid()
        
        l = Label(frame, text="Critical Hit Table", font=('Arial', 15, 'bold'), foreground='blue')
        l.grid(column=0, row=0, pady=5)
        
        f = 0
        s = 3
        first = int(random.randint(1,100))
        second = int(random.randint(1,10))
        if 11 <= first <= 20:
            f = 1
        elif 11 <= first <= 30:
            f = 2
        elif 11 <= first <= 40:
            f = 3
        elif 11 <= first <= 50:
            f = 4
        elif 11 <= first <= 60:
            f = 5
        elif 11 <= first <= 70:
            f = 6
        elif 11 <= first <= 80:
            f = 7
        elif 11 <= first <= 90:
            f = 8
        elif 11 <= first <= 99:
            f = 9
        elif first == 100:
            f = 10
        
        if 4 <= second <= 6:
            s = 4
        elif 7 <= second <= 9:
            s = 5
        elif second == 10:
            s = 6
        
        if f == 5 or f == 10:
            lc = Label(frame, text=ct[f][0:3])
            lc.grid(column=0, row=2)
            b = Button(frame, text="Exit", command=w.destroy)
            b.grid(column=0, row=3, pady=5)
        else:
            lc = Label(frame, text=ct[f][0:3])
            lc.grid(column=0, row=2)
            le = Label(frame, text=ct[f][s])
            le.grid(column=0, row=3)
            b = Button(frame, text="Exit", command=w.destroy)
            b.grid(column=0, row=4, pady=5)
        
        w.mainloop()
