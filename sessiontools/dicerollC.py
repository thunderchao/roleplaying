#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.constants import *
from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
import random
import itertools

class Roller:
    def dice_roller(self, *args):
        m = int(m_e.get())
        d = int(d_e.get())
        a = int(a_e.get())
	    
        sides = 0
        
        #for _ in itertools.repeat(d, m):
        for i in range(m):
            side = random.randint(1,d)
            sides += side
        roll = str(m) + "d" + str(d) + "+" + str(a)
        value = sides + a
        lb.insert(END, (roll+' ('+str(value)+')'))
        m_e.focus()
        
    def clear(self):
        lb.delete(0, END)
	
    #set up window as init
    def __init__(self):
        global lb, m_e, d_e, a_e
        w = Tk()
        w.title("Dice Roll")
        w.geometry('+900+100')
        frame = Frame(w)
        frame.grid(column=0, row=0)
        
        l = Label(frame, text='Dice Roll', font=('Arial', 15, 'bold'), foreground='blue')
        l.grid(column=0, row=0, columnspan=7)
        
        lb = Listbox(frame, selectmode=EXTENDED, height=10, width=15)
        lb.grid(column=0, row=1, rowspan=4)
        yscroll = Scrollbar(frame, command=lb.yview, orient=VERTICAL)
        yscroll.grid(column=1, row=1, rowspan=4, sticky=(N,W,S))
        lb.configure(yscrollcommand=yscroll.set)
        
        m_e = Entry(frame, width=2)
        m_e.insert(0, '1')
        m_e.config(justify=CENTER)
        m_e.grid(column=2, row=1, padx=5, pady=5, sticky=N)
        
        d_l = Label(frame, text='d')
        d_l.grid(column=3, row=1, pady=5, sticky=N)
        
        d_e = Entry(frame, width=2)
        d_e.insert(0, '20')
        d_e.config(justify=CENTER)
        d_e.grid(column=4, row=1, padx=5, pady=5, sticky=N)
        
        plus_l = Label(frame, text='+')
        plus_l.grid(column=5, row=1, pady=5, sticky=N)
        
        a_e = Entry(frame, width=2)
        a_e.insert(0, '0')
        a_e.config(justify=CENTER)
        a_e.grid(column=6, row=1, padx=5, pady=5, sticky=N)
        
        b = Button(frame, text="Roll and save", command=self.dice_roller)
        b.grid(column=2, row=2, columnspan=5, sticky=N)
        b.bind('<Key-Return>', self.dice_roller)
        
        clear_b = Button(frame, text="Clear list", command=self.clear)
        clear_b.grid(column=2, row=3, columnspan=5, sticky=S, pady=5)
        
        quit_b = Button(frame, text="Exit", command=w.destroy)
        quit_b.grid(column=2, row=4, columnspan=5)
        
        w.mainloop()
	
