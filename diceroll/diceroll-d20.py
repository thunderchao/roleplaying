#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       diceroll-d20.py
#       
#       Copyright 2012 Nathaniel Ray Pickett <@thunderchao>
#       
#       Use this interactive program to make a series of dice rolls.
#       This variant only rolls d20s and ackowledges Crits. It's quite simple.
#
#       Enjoy!
#

import random
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
                                                                             
                                the d20er                                    
""")

print(Style.RESET_ALL + 'roll some dice!')

times = int(input('how many times do you want to roll? '))

while times > 0:
    roll = random.randint(1,20)         #only rolls 1d20
    if roll == 20:                      #yay for crits!
        print('CRITICAL!', end=', ')
    else:
        print(roll, end=", ")
    times -= 1

