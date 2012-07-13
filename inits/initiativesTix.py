#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       initiativesTix.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       For tracking your D&D initiatives! Now with foci, key bindings,
#       shrinkage, and balloons!
#
#       Sorting after editing still doesn't work quite right...
#
#       Version 1.3
#       

#import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
import random

#define functions and classes
def delete_item():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass
        
def add_item3():
    nums = random.randint(1,20) + int(bonus_e.get())
    whole = str(nums).rjust(2, '0'), name_e.get()
    listbox.insert(END, whole)
    name_e.focus()
    name_e.delete(0, END)
    bonus_e.delete(0, END)
    bonus_e.insert(END, '0')

def add_item_b(self):
    nums = random.randint(1,20) + int(bonus_e.get())
    whole = str(nums).rjust(2, '0'), name_e.get()
    listbox.insert(END, whole)
    name_e.focus()
    name_e.delete(0, END)
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
        listbox.yview(above_i)
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
        listbox.yview(below_i)
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

        self.lf = LabelFrame(top, text='Edit Entry')
        self.lf.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        
        self.l = Label(self.lf, text='Format: "## name"')
        self.l.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
                
        self.e = Entry(self.lf, width=15)
        self.e.insert(0, '')
        self.e.focus()
        self.e.bind("<Key-Return>", self.okb)
        self.e.grid(column=0, row=2, padx=5, pady=5)

        b = Button(self.lf, text="ok", command=self.ok)
        b.bind("<Key-Return>", self.okb)
        b.grid(column=1, row=2, padx=5, pady=5)

    def ok(self):
        self.result = self.e.get()
        self.top.destroy()
    
    def okb(self, b):
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

#set up window
main_window = Tk()
main_window.title("Initiative Tracker")
frame = Frame(main_window, relief=RIDGE, borderwidth=2)
frame.grid(column=0, row=0, columnspan=6, rowspan=7)

toplabel = Label(frame, text="Initiative Tracker")
toplabel.grid(column=0, row=0, columnspan=6, pady=5)

#the listbox area
listbox = Listbox(frame, selectmode=BROWSE, height=9)
listbox.grid(column=0, row=1, columnspan=3, rowspan=5)

yscroll = Scrollbar(frame, command=listbox.yview, orient=VERTICAL)
yscroll.grid(column=3, row=1, rowspan=5, sticky=(N,S))
listbox.configure(yscrollcommand=yscroll.set)

up_b = Button(frame, text="˄", command=move_up, width=3)
up_b.grid(column=0, row=6)

down_b = Button(frame, text="˅", command=move_down, width=3)
down_b.grid(column=1, row=6)

sort_b = Button(frame, text='sort', command=sort_list, width=8)
sort_b.grid(column=2, row=6)

#the add labelframe
add_f = LabelFrame(frame, text="Add a new entry")
add_f.grid(column=4, row=1, columnspan=2, rowspan=3, padx=5)

name_e = Entry(add_f, width=15)
name_e.focus()
name_e.insert(0, '')
name_e.bind("<Key-Return>", add_item_b)
name_e.grid(column=5, row=2, padx=2, pady=2)

bonus_e = Entry(add_f, width=2)
bonus_e.insert(0, '0')
bonus_e.bind("<Key-Return>", add_item_b)
bonus_e.grid(column=6, row=2, padx=2, pady=2)
bonus_e.config(justify=CENTER)

bal = Balloon(main_window, initwait=500)
bal.bind_widget(name_e, balloonmsg="Enter name here")
bal.bind_widget(bonus_e, balloonmsg="Enter initiative bonus here")

add_b = Button(add_f, text="roll and add", command=add_item3, width=16)
add_b.bind("<Key-Return>", add_item_b)
add_b.grid(column=5, row=3, columnspan=2, padx=5, pady=5)

#the other stuff
edit_b = Button(frame, text="edit selected", command=edit_item, width=16)
edit_b.grid(column=4, row=4, columnspan=3, pady=4)

del_b = Button(frame, text="delete selected", command=delete_item, width=16)
del_b.grid(column=4, row=5, columnspan=3, pady=4)

quit_b = Button(frame, text="exit", command=main_window.destroy, width=16)
quit_b.grid(column=4, row=6, columnspan=3, pady=4)

#botlabel = Label(frame, text="© Nathaniel Ray Pickett")
#botlabel.grid(column=4, row=8, columnspan=2, padx=5, sticky=E)

main_window.mainloop()
