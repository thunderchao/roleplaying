#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       initiatives.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       For tracking your D&D initiatives!
#
#       Version 1.0
#       

import tkinter
from tkinter.constants import *
import random

class Inits:
    #define functions and classes
    def delete_item(self):
        try:
            self.index = self.listbox.curselection()[0]
            self.listbox.delete(self.index)
        except IndexError:
            pass
        
    def add_item(self):
        self.listbox.insert(END, self.addentry.get())
        self.addentry.delete(0, END)
    
    def change_item(self):
        try:
            self.index = self.listbox.curselection()[0]
            self.item_to_change = self.listbox.get(self.index)
            return item_to_change
        except IndexError:
            pass

    def sort_list(self):
        temp_list = list(self.listbox.get(0, END))
        temp_list.sort(key=lambda thing: thing[0])
        self.listbox.delete(0, END)
        for item in temp_list:
            self.listbox.insert(END, item)

    class AskBox:
        def __init__(self, parent):
            top = self.top = tkinter.Toplevel(parent)
            top.title('Add bonus')
            top.geometry('+620+310')

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


    def roll_it(self):
        try:
            self.index = self.listbox.curselection()[0]
            sel = self.listbox.get(self.index)
        
            self.main_window.update()
            self.ask = self.AskBox(self.main_window)
            self.main_window.wait_window(self.ask.top)
        
            self.rand = random.randint(1,20) + int(self.ask.result)
            self.this = str(self.rand).rjust(2, '0'), sel
            self.listbox.delete(self.index)
        except IndexError:
            self.index = END
        self.listbox.insert(self.index, self.this)

    #main window as init
    def __init__(self):
        main_window = self.main_window = tkinter.Tk()
        main_window.title("Initiative Tracker")
        main_window.geometry('-620+100')
        frame = self.frame = tkinter.Frame(main_window, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH, expand=1)

        self.toplabel = tkinter.Label(frame, text="Initiative Tracker")
        self.toplabel.grid(column=0, row=0, columnspan=4, pady=5)

        l =[]
        listbox = self.listbox = tkinter.Listbox(frame, selectmode=BROWSE, height=6)
        for item in l:
            listbox.insert(END, item)
        listbox.grid(column=0, row=1, rowspan=3)

        self.yscroll = tkinter.Scrollbar(frame, command=listbox.yview, orient=VERTICAL)
        self.yscroll.grid(column=1, row=1, rowspan=3, sticky=(N,S,W))
        listbox.configure(yscrollcommand=self.yscroll.set)

        self.addentry = tkinter.Entry(frame, width=20)
        self.addentry.insert(0, '')
        self.addentry.grid(column=2, row=1, columnspan=2, padx=5, pady=5)

        self.addbutton = tkinter.Button(frame, text="add", command=self.add_item)
        self.addbutton.grid(column=2, row=2)

        self.rollbutton = tkinter.Button(frame, text='roll for selected', command=self.roll_it)
        self.rollbutton.grid(column=3, row=2)

        self.sortbutton = tkinter.Button(frame, text='sort', command=self.sort_list)
        self.sortbutton.grid(column=2, row=3)

        self.delbutton = tkinter.Button(frame, text="delete selected", command=self.delete_item)
        self.delbutton.grid(column=3, row=3)

        self.botlabel = tkinter.Label(frame, text="© Nathaniel Ray Pickett")
        self.botlabel.grid(column=0, row=4, columnspan=2, padx=5, sticky=W)

        self.quitbutton = tkinter.Button(frame, text="Exit", command=main_window.destroy)
        self.quitbutton.grid(column=2, row=4, columnspan=2, pady=5)

        main_window.mainloop()
