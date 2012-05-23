#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       diceroll-quick.py
#       
#       Copyright 2012 Nathaniel Ray Pickett <@thunderchao>
#       
#       Use this interactive program to make a quick dice roll.
#       This variant is stripped down for quick rolls that don't need saving.
#
#       Enjoy!
#

import random
import itertools
import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.GREEN + Back.WHITE + """
                                                                             
      888 d8b                                       888 888                  
      888 Y8P                                       888 888                  
      888                                           888 888                  
  .d88888 888  .d8888b .d88b.       888d888 .d88b.  888 888  .d88b.  888d888 
 d88" 888 888 d88P"   d8P  Y8b      888P"  d88""88b 888 888 d8P  Y8b 888P"   
 888  888 888 888     88888888      888    888  888 888 888 88888888 888     
 Y88b 888 888 Y88b.   Y8b.          888    Y88..88P 888 888 Y8b.     888     
  "Y88888 888  "Y8888P "Y8888       888     "Y88P"  888 888  "Y8888  888     
                                                                             
                                the quickie                                  
""")

print(Style.RESET_ALL + 'roll some dice!')

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

m = int(input('how many dice? '))       #integers only on these three
d = int(input('how many sides? '))
a = int(input('plus how much? '))
roll = dice_roller(m, d, a)             #only rolls once

