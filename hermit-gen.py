#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       hermit-gen.py
#       
#       Copyright 2012 Nathaniel Ray <Nathaniel Ray@THUNDERCLEESE>
#       
#       This program is based on Rolang's Random Hermit Generator
#       (http://www.rolang.com/archives/446) but slightly modified.
#       
#       

import random

obsession = {1 : 'meditation',
             2 : 'prayer',
             3 : 'math',
             4 : 'botany',
             5 : 'magic',
             6 : 'animal husbandry',
             7 : 'cryptozoology',
             8 : 'ancient languages',
             9 : 'supernatural events',
             10: 'the apocalypse', }

converse = { 1 : 'no one (he\'s mute)',
             2 : 'birds',
             3 : 'plants',
             4 : 'animals',
             5 : 'rocks',
             6 : 'invisible friend',
             7 : 'ghosts',
             8 : 'puppets',
             9 : 'dead mother\'s corpse',
             10: 'penis', }

tolerate = { 1 : 'no one',
             2 : 'children',
             3 : 'sick people',
             4 : 'lovers',
             5 : 'warriors',
             6 : 'minstrels',
             7 : 'prostitutes',
             8 : 'peasants',
             9 : 'perverts',
             10: 'anyone with food', }

quirk = {    1 : 'talks only in rhyme',
             2 : 'crawls on all fours',
             3 : 'calls everyone the same name',
             4 : 'farts constantly',
             5 : 'collects other\'s hair',
             6 : 'talks backwards',
             7 : 'herds cats',
             8 : 'can only speak out of his butt',
             9 : 'cannot touch the ground with his feet',
             10: 'eats nothing without ketchup', }

secret = {   1 : 'related to a party member',
             2 : 'of noble birth',
             3 : 'a great swordsman',
             4 : 'wanted for crimes',
             5 : 'a former entertainer',
             6 : 'a polymorphed monster',
             7 : 'a woman',
             8 : 'rich beyond belief',
             9 : 'displaced in time',
             10: 'that he has none', }

print('          Random Hermit Generator!')
print('                    v1.1')

nr = 5
while nr >= 0:
    if nr == 5:
        obs_res = obsession[random.randint(1,10)]
        nr -= 1
    if nr == 4:
        con_res = converse[random.randint(1,10)]
        nr -= 1
    if nr == 3:
        tol_res = tolerate[random.randint(1,10)]
        nr -= 1
    if nr == 2:
        qui_res = quirk[random.randint(1,10)]
        nr -= 1
    if nr == 1:
        sec_res = secret[random.randint(1,10)]
        nr -= 1
    if nr == 0:
        print('\nYour randomly generated hermit is obsessed with %s,' % (obs_res))
        print('converses only with %s, and only tolerates %s.' % (con_res, tol_res))
        print('Curiously, he constantly %s and in reality,' % (qui_res))
        print('he is actually %s!\n' % (sec_res))
        a = input('Roll up another one? (y/n) ')
        if a == 'y':
            nr = 5
        else:
            break 
