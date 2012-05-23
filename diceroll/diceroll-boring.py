#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       diceroll-boring.py
#       
#       Copyright 2012 Nathaniel Ray Pickett <@thunderchao>
#       
#       Use this interactive program to make a set of dice rolls.
#       This variant is a boring one with no color or ASCII art that
#       is otherwise identical to the original.
#
#       Enjoy!
#

import random
import itertools

print('dice roller: the boring one')

print('roll some dice!')

def dice_roller(m, d, a):
    #what we're going for: 3d6+10
    sides = 0
    for _ in itertools.repeat(d, m):    #this makes accurate dice rolls
        side = random.randint(1,d)
        sides += side
    roll = str(m) + "d" + str(d) + "+" + str(a)
    value = sides + a
    print('you rolled', roll, 'getting', value)
    return value

times = int(input('how many times do you want to roll? '))
roll_set = {}                           #saving the set in a dict

while times > 0:
    roll = input('\nname this roll: ')  #make sure each name is unique
    m = int(input('how many dice? '))   #integers only on these three
    d = int(input('how many sides? '))
    a = int(input('plus how much? '))
    roll_set[roll] = dice_roller(m, d, a)
    times -= 1

print(roll_set)
