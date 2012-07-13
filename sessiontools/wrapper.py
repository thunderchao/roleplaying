#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       wrapper.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       All-in-one D&D program.
#
#       Version 1.0
#  

from tkinter.constants import *
from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
import initsTixC, dicerollC, critC

#define the functions
def load_ql():
    try:
        ql = open('ql.txt', 'rt')
        ql_contents = ql.read()
        ql_t.delete(1.0, END)
        ql_t.insert(1.0, ql_contents)
        ql.close()
    except IOError:
        pass 
    
def save_ql():
    ql = open('ql.txt', 'wt')
    ql_contents = ql_t.get(1.0, END)
    ql.write(ql_contents)
    ql.close()
    
def load_a():
    try:
        a = open('a.txt', 'rt')
        a_contents = a.read()
        a_t.delete(1.0, END)
        a_t.insert(1.0, a_contents)
        a.close()
    except IOError:
        pass 
    
def save_a():
    a = open('a.txt', 'wt')
    a_contents = a_t.get(1.0, END)
    a.write(a_contents)
    a.close()
    
def load_b():
    try:
        b = open('b.txt', 'rt')
        b_contents = b.read()
        b_t.delete(1.0, END)
        b_t.insert(1.0, b_contents)
        b.close()
    except IOError:
        pass 
    
def save_b():
    b = open('b.txt', 'wt')
    b_contents = b_t.get(1.0, END)
    b.write(b_contents)
    b.close()
    
def load_c():
    try:
        c = open('c.txt', 'rt')
        c_contents = c.read()
        c_t.delete(1.0, END)
        c_t.insert(1.0, c_contents)
        c.close()
    except IOError:
        pass 
    
def save_c():
    c = open('c.txt', 'wt')
    c_contents = c_t.get(1.0, END)
    c.write(c_contents)
    c.close()

def save_all():
    save_ql()
    save_a()
    save_b()
    save_c()
    root.destroy()

root = Tk()
root.title('D&D Session Tools')
root.geometry('+100+100')
frame = Frame(root)
frame.grid()

top_l = Label(frame, text='D&D Session Tools', font=('Arial', 15, 'bold'), foreground='blue')
top_l.grid(column=0, row=0, columnspan=8, sticky=N, pady=5)

status = Label(frame)
status.grid(column=0, row=8, columnspan=6, sticky=W, padx=10) 

#left side
ql_lf = LabelFrame(frame, text='Questlog')
ql_lf.grid(column=0, row=1, columnspan=3, sticky=N, padx=5, pady=10)

ql_t = Text(ql_lf)
ql_t.grid(column=0, row=1, columnspan=2, rowspan=5)
ql_t.config(width=25, height=30, tabs=16)

ql_sby = Scrollbar(ql_lf, command=ql_t.yview, orient=VERTICAL)
ql_sby.grid(column=2, row=1, rowspan=5, sticky=(N,S,W))
ql_t.configure(yscrollcommand=ql_sby.set)

ql_load = Button(ql_lf, text='Load', command=load_ql)
ql_load.grid(column=0, row=6, padx=5, pady=6)

ql_save = Button(ql_lf, text='Save', command=save_ql)
ql_save.grid(column=1, row=6, padx=5, pady=6)

#the center
data_nb = Notebook(frame)
data_nb.grid(column=3, row=1, columnspan=4, rowspan=5, sticky=N, pady=5)
tab_a = Frame(data_nb)
tab_b = Frame(data_nb)
tab_c = Frame(data_nb)
data_nb.add(tab_a, text=' Notes A ')
data_nb.add(tab_b, text=' Notes B ')
data_nb.add(tab_c, text=' Notes C ')

##tab a
a_t = Text(tab_a, width=45, height=30)
a_t.config(wrap=WORD)
a_t.grid(column=3, row=1, columnspan=3, rowspan=5)

a_sb = Scrollbar(tab_a, command=a_t.yview, orient=VERTICAL)
a_sb.grid(column=6, row=1, rowspan=5, sticky=(N,S,W))
a_t.configure(yscrollcommand=a_sb.set)

a_load = Button(tab_a, text='Load', command=load_a)
a_load.grid(column=3, row=6, padx=5, pady=5)
a_save = Button(tab_a, text='Save', command=save_a)
a_save.grid(column=4, row=6, padx=5, pady=5)

##tab b
b_t = Text(tab_b, width=45, height=30)
b_t.config(wrap=WORD)
b_t.grid(column=3, row=1, columnspan=3, rowspan=5)

b_sb = Scrollbar(tab_b, command=b_t.yview, orient=VERTICAL)
b_sb.grid(column=6, row=1, rowspan=5, sticky=(N,S,W))
b_t.configure(yscrollcommand=b_sb.set)

b_load = Button(tab_b, text='Load', command=load_b)
b_load.grid(column=3, row=6, padx=5, pady=5)
b_save = Button(tab_b, text='Save', command=save_b)
b_save.grid(column=4, row=6, padx=5, pady=5)

##tab c
c_t = Text(tab_c, width=45, height=30)
c_t.config(wrap=WORD)
c_t.grid(column=3, row=1, columnspan=3, rowspan=5)

c_sb = Scrollbar(tab_c, command=c_t.yview, orient=VERTICAL)
c_sb.grid(column=6, row=1, rowspan=5, sticky=(N,S,W))
c_t.configure(yscrollcommand=c_sb.set)

c_load = Button(tab_c, text='Load', command=load_c)
c_load.grid(column=3, row=6, padx=5, pady=5)
c_save = Button(tab_c, text='Save', command=save_c)
c_save.grid(column=4, row=6, padx=5, pady=5)

#right side
tools_lf = LabelFrame(frame, text='Tools')
tools_lf.grid(column=7, row=1, sticky=N, padx=5, pady=10)

in_b = Button(tools_lf, text='Initiative Tracker', width=18, command=initsTixC.Inits)
in_b.grid(column=7, row=1, padx=5)

dr_b = Button(tools_lf, text='Dice Roll', width=18, command=dicerollC.Roller)
dr_b.grid(column=7, row=2, padx=5, pady=5)

tr_b = Button(tools_lf, text='The Treasury', width=18)#, command=?
tr_b.grid(column=7, row=3, padx=5)

ct_b = Button(tools_lf, text='Critical Hit Table', width=18, command=critC.Table)
ct_b.grid(column=7, row=4, padx=5, pady=5)

ma_b = Button(tools_lf, text='Maps', width=18)#, command=?
ma_b.grid(column=7, row=5, padx=5)

ot_b = Button(tools_lf, text='Other', width=18)#, command=?
ot_b.grid(column=7, row=6, padx=5, pady=5)

se_b = Button(frame, text='Save all & Exit', width=18, command=save_all)
se_b.grid(column=7, row=7, sticky=S)

exit_b = Button(frame, text='Exit', width=18, command=root.destroy)
exit_b.grid(column=7, row=8, pady=5, sticky=S)

b = Balloon(frame, statusbar=status, initwait=0)
b.bind_widget(top_l, statusmsg='©2012 Nathaniel Ray Pickett @thunderchao')
b.bind_widget(ql_load, statusmsg='Load the saved questlog')
b.bind_widget(ql_save, statusmsg='Save the questlog')
b.bind_widget(a_load, statusmsg='Load the saved data for this tab')
b.bind_widget(a_save, statusmsg='Save the data in this tab')
b.bind_widget(b_load, statusmsg='Load the saved data for this tab')
b.bind_widget(b_save, statusmsg='Save the data in this tab')
b.bind_widget(c_save, statusmsg='Load the saved data for this tab')
b.bind_widget(c_save, statusmsg='Save the data in this tab')
b.bind_widget(in_b, statusmsg='Launch the initiatives tracker')
b.bind_widget(dr_b, statusmsg='Launch the dice roller')
b.bind_widget(tr_b, statusmsg='Launch the treasure depot')
b.bind_widget(ct_b, statusmsg='Launch the critical hit/miss tables')
b.bind_widget(ma_b, statusmsg='Launch the map')
b.bind_widget(ot_b, statusmsg='Launch the other tool')

load_ql()
load_a()
load_b()
load_c()

root.mainloop()



