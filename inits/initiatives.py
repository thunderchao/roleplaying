#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       initiatives.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       For tracking your D&D initiatives!
#       

import tkinter
from tkinter.constants import *
import random

#define functions and classes
def delete_item():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass
        
def add_item():
    listbox.insert(END, addentry.get())
    addentry.delete(0, END)

def sort_list():
    temp_list = list(listbox.get(0, END))
    temp_list.sort(key=lambda thing: thing[0])
    listbox.delete(0, END)
    for item in temp_list:
        listbox.insert(END, item)

class AskBox:
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        top.title('Add bonus')

        self.l = tkinter.Label(top, text='Add initiative bonus')
        self.l.grid(column=0, row=0, columnspan=2)
                
        self.e = tkinter.Entry(top, width=10)
        self.e.insert(0, '0')
        self.e.grid(column=0, row=1, padx=3, pady=5)

        b = tkinter.Button(top, text="ok", command=self.ok)
        b.grid(column=1, row=1, padx=3, pady=5)

    def ok(self):
        self.result = self.e.get()
        self.top.destroy()


def roll_it():
    try:
        index = listbox.curselection()[0]
        sel = listbox.get(index)
        
        main_window.update()
        ask = AskBox(main_window)
        main_window.wait_window(ask.top)
        
        rand = random.randint(1,20) + int(ask.result)
        this = str(rand).rjust(2, '0'), sel
        listbox.delete(index)
    except IndexError:
        index = END
    listbox.insert(index, this)

#set up window
main_window = tkinter.Tk()
main_window.title("Initiative Tracker")
frame = tkinter.Frame(main_window, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

toplabel = tkinter.Label(frame, text="Initiative Tracker")
toplabel.grid(column=0, row=0, columnspan=4, pady=5)

l =[]
listbox = tkinter.Listbox(frame, selectmode=BROWSE, height=6)
for item in l:
    listbox.insert(END, item)
listbox.grid(column=0, row=1, rowspan=3)

yscroll = tkinter.Scrollbar(frame, command=listbox.yview, orient=VERTICAL)
yscroll.grid(column=1, row=1, rowspan=3, sticky=(N,S,W))
listbox.configure(yscrollcommand=yscroll.set)

addentry = tkinter.Entry(frame, width=20)
addentry.insert(0, '')
addentry.grid(column=2, row=1, columnspan=2, padx=5, pady=5)

addbutton = tkinter.Button(frame, text="add", command=add_item)
addbutton.grid(column=2, row=2)

rollbutton = tkinter.Button(frame, text='roll for selected', command=roll_it)
rollbutton.grid(column=3, row=2)

sortbutton = tkinter.Button(frame, text='sort', command=sort_list)
sortbutton.grid(column=2, row=3)

delbutton = tkinter.Button(frame, text="delete selected", command=delete_item)
delbutton.grid(column=3, row=3)

botlabel = tkinter.Label(frame, text="© Nathaniel Ray Pickett")
botlabel.grid(column=0, row=4, columnspan=2, padx=5, sticky=W)

quitbutton = tkinter.Button(frame, text="Exit", command=main_window.destroy)
quitbutton.grid(column=2, row=4, columnspan=2, pady=5)

main_window.mainloop()
