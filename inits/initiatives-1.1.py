#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       initiatives-1.1.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       For tracking your D&D initiatives! Now with increased control,
#       more sexiness, lots more buttons, and a fancy new layout.
#
#       Sorting after editing still doesn't work quite right...
#
#       Version 1.1
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
        
def add_item2():
    nums = int(roll_e.get()) + int(bonus_e.get())
    whole = str(nums).rjust(2, '0'), name_e.get()
    listbox.insert(END, whole)
    name_e.delete(0, END)
    roll_e.delete(0, END)
    bonus_e.delete(0, END)
    bonus_e.insert(END, '0')

def move_up():
    try:
        selected = listbox.curselection()[0]
        selected_i = listbox.index(selected)
        selected_v = listbox.get(selected_i)
        
        above_i = selected_i - 1
        
        listbox.delete(selected_i)
        listbox.insert(above_i, selected_v)
        listbox.select_set(above_i)
        listbox.activate(above_i)
    except IndexError:
        pass

def move_down():
    try:
        selected = listbox.curselection()[0]
        selected_i = listbox.index(selected)
        selected_v = listbox.get(selected_i)
        
        below_i = selected_i + 1
        
        listbox.delete(selected_i)
        listbox.insert(below_i, selected_v)
        listbox.select_set(below_i)
        listbox.activate(below_i)
    except IndexError:
        pass

def sort_list():
    temp_list = list(listbox.get(0, END))
    temp_list.sort(key=lambda thing: thing[0])
    listbox.delete(0, END)
    for item in temp_list:
        listbox.insert(END, item)

class EditBox:
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        top.title('Edit Entry')

        self.lf = tkinter.LabelFrame(top, text='Edit Entry')
        self.lf.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        
        self.l = tkinter.Label(self.lf, text='Format: "## name"')
        self.l.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
                
        self.e = tkinter.Entry(self.lf, width=15)
        self.e.insert(0, '')
        self.e.grid(column=0, row=2, padx=5, pady=5)

        b = tkinter.Button(self.lf, text="ok", command=self.ok)
        b.grid(column=1, row=2, padx=5, pady=5)

    def ok(self):
        self.result = self.e.get()
        self.top.destroy()

def edit_item():
    try:
        index = listbox.curselection()[0]
        item_to_change = listbox.get(index)
        
        main_window.update()
        edit = EditBox(main_window)
        main_window.wait_window(edit.top)
        
        item_to_change = edit.result
        listbox.delete(index)
    except IndexError:
        pass
    listbox.insert(index, item_to_change)

def roll_it2():
    try:
        rand = random.randint(1,20)
        roll_e.insert(0, rand)
    except IndexError:
        pass

#set up window
main_window = tkinter.Tk()
main_window.title("Initiative Tracker")
frame = tkinter.Frame(main_window, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=5)

toplabel = tkinter.Label(frame, text="Initiative Tracker")
toplabel.grid(column=0, row=0, columnspan=7, pady=5)

#the listbox area
listbox = tkinter.Listbox(frame, selectmode=BROWSE, height=11)
listbox.grid(column=0, row=1, columnspan=3, rowspan=7)

yscroll = tkinter.Scrollbar(frame, command=listbox.yview, orient=VERTICAL)
yscroll.grid(column=3, row=1, rowspan=7, sticky=(N,S))
listbox.configure(yscrollcommand=yscroll.set)

up_b = tkinter.Button(frame, text="˄", command=move_up)
up_b.grid(column=0, row=8)

down_b = tkinter.Button(frame, text="˅", command=move_down)
down_b.grid(column=1, row=8)

sort_b = tkinter.Button(frame, text='sort', command=sort_list)
sort_b.grid(column=2, row=8)

#the add labelframe
add_f = tkinter.LabelFrame(frame, text="Add a new entry")
add_f.grid(column=4, row=1, columnspan=2, rowspan=3, padx=5)

name_e = tkinter.Entry(add_f, width=15)
name_e.insert(0, '')
name_e.icursor(0)
name_e.grid(column=5, row=2, columnspan=3, padx=5, pady=2)

roll_e = tkinter.Entry(add_f, width=2)
roll_e.insert(0, '')
roll_e.grid(column=5, row=3, padx=5, pady=2)

plus_l = tkinter.Label(add_f, text="+")
plus_l.grid(column=6, row=3)

bonus_e = tkinter.Entry(add_f, width=2)
bonus_e.insert(0, '0')
bonus_e.grid(column=7, row=3, padx=5, pady=2)

roll_b = tkinter.Button(add_f, text='roll', command=roll_it2)
roll_b.grid(column=5, row=4, padx=5, pady=2)

add_b = tkinter.Button(add_f, text="add", command=add_item2)
add_b.grid(column=7, row=4, padx=5, pady=2)

#the other stuff
edit_b = tkinter.Button(frame, text="edit selected", command=edit_item)
edit_b.grid(column=4, row=5, columnspan=3, pady=2)

del_b = tkinter.Button(frame, text="delete selected", command=delete_item)
del_b.grid(column=4, row=6, columnspan=3, pady=2)

quit_b = tkinter.Button(frame, text="exit", command=main_window.destroy)
quit_b.grid(column=4, row=7, columnspan=3, pady=2)

botlabel = tkinter.Label(frame, text="© Nathaniel Ray Pickett")
botlabel.grid(column=4, row=8, columnspan=2, padx=5, sticky=E)

main_window.mainloop()
