#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       initiatives-1.2.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       For tracking your D&D initiatives! Now with tweaked layout,
#       tweaked tweaks, tooltips, and ttk!
#
#       Sorting after editing still doesn't work quite right...
#
#       Version 1.2
#       

#import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
import random

class Inits:
    #define functions and classes
    def delete_item(self):
        try:
            index = listbox.curselection()[0]
            listbox.delete(index)
        except IndexError:
            pass
        
    def add_item3(self):
        nums = random.randint(1,20) + int(bonus_e.get())
        whole = str(nums).rjust(2, '0'), name_e.get()
        listbox.insert(END, whole)
        name_e.focus()
        name_e.delete(0, END)
        bonus_e.delete(0, END)
        bonus_e.insert(END, '0')

    def move_up(self):
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

    def move_down(self):
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

    def sort_list(self):
        temp_list = list(listbox.get(0, END))
        temp_list.sort(key=lambda thing: thing[0])
        listbox.delete(0, END)
        for item in temp_list:
            listbox.insert(END, item)

    class EditBox:
        def __init__(self, parent):
            top = self.top = Toplevel(parent)
            top.title('Edit Entry')
            top.geometry('+900+100')

            self.lf = LabelFrame(top, text='Edit Entry')
            self.lf.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        
            self.l = Label(self.lf, text='Format: "## name"')
            self.l.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
                
            self.e = Entry(self.lf, width=15)
            self.e.insert(0, '')
            self.e.grid(column=0, row=2, padx=5, pady=5)

            b = Button(self.lf, text="ok", command=self.ok)
            b.grid(column=1, row=2, padx=5, pady=5)

        def ok(self):
            self.result = self.e.get()
            self.top.destroy()

    def edit_item(self):
        try:
            index = listbox.curselection()[0]
            item_to_change = listbox.get(index)
        
            main_window.update()
            edit = self.EditBox(main_window)
            main_window.wait_window(edit.top)
        
            item_to_change = edit.result
            listbox.delete(index)
        except IndexError:
            pass
        listbox.insert(index, item_to_change)

    #set up window as init
    def __init__(self):
        global listbox, main_window, name_e, bonus_e
        
        main_window = Tk()
        main_window.title("Initiative Tracker")
        main_window.geometry('+900+100')
        frame = Frame(main_window, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH, expand=5)

        toplabel = Label(frame, text="Initiative Tracker", font=('Arial', 15, 'bold'), foreground='blue')
        toplabel.grid(column=0, row=0, columnspan=7, pady=5)

        #the listbox area
        listbox = Listbox(frame, selectmode=EXTENDED, height=11)
        listbox.grid(column=0, row=1, columnspan=3, rowspan=7)

        yscroll = Scrollbar(frame, command=listbox.yview, orient=VERTICAL)
        yscroll.grid(column=3, row=1, rowspan=7, sticky=(N,S))
        listbox.configure(yscrollcommand=yscroll.set)

        up_b = Button(frame, text="˄", command=self.move_up, width=3)
        up_b.grid(column=0, row=8)

        down_b = Button(frame, text="˅", command=self.move_down, width=3)
        down_b.grid(column=1, row=8)

        sort_b = Button(frame, text='sort', command=self.sort_list, width=8)
        sort_b.grid(column=2, row=8)

        #the add labelframe
        add_f = LabelFrame(frame, text="Add a new entry")
        add_f.grid(column=4, row=1, columnspan=2, rowspan=3, padx=5)

        name_e = Entry(add_f, width=15)
        name_e.insert(0, '')
        name_e.grid(column=5, row=2, padx=2, pady=2)

        bonus_e = Entry(add_f, width=2)
        bonus_e.insert(0, '0')
        bonus_e.grid(column=6, row=2, padx=2, pady=2)
        bonus_e.config(justify=CENTER)

        add_b = Button(add_f, text="roll and add", command=self.add_item3, width=16)
        add_b.grid(column=5, row=3, columnspan=2, padx=5, pady=5)

        #the other stuff
        edit_b = Button(frame, text="edit selected", command=self.edit_item, width=16)
        edit_b.grid(column=4, row=4, columnspan=3, pady=4)

        del_b = Button(frame, text="delete selected", command=self.delete_item, width=16)
        del_b.grid(column=4, row=5, columnspan=3)

        quit_b = Button(frame, text="exit", command=main_window.destroy, width=16)
        quit_b.grid(column=4, row=8, columnspan=3, pady=4, sticky=S)

        status = Label(frame, width=16)
        status.grid(column=4, row=7, columnspan=3, padx=5)

        b = Balloon(frame, statusbar=status, initwait=0)
        b.bind_widget(name_e, statusmsg='Enter name')
        b.bind_widget(bonus_e, statusmsg='Enter init. bonus')

        main_window.mainloop()
