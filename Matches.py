#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
On the table there are 40 matches. Players take the matches from the table in turns.
In each turn a player can take 1,2 or 3 matches. The player who takes the last match wins.
"""


from random import randint
from time import sleep


def matches_game():
    match_table = 'I' * 40
    i = 0
    while True and len(match_table) > 0:
        print('Part {}'.format(i+1))
        print(match_table)
        if i % 2 == 0:

            print('\n\t\t\tPLAYER TURN')
            a = int(input('number of matches to take:'))
            if 3 > len(match_table) > 1:
                print('On the table is only {} matches'.format(len(match_table)))
                a = int(input('number of matches to take:'))
                if a > len(match_table):
                    print('Again you wanted to make an illegal move. GAME OVER :(')
                    break
            elif a > 3 or a < 1:
                print('number of matches to take 1,2 OR 3')
                a = int(input('number of matches to take:'))
                if a > 3 or a < 1:
                    print("You can't count to three.")
                    print('\n\n\t\t\t\t\t\t\t Game over :((')
                    break
        else:
            print('\n\t\t\tCOMPUTER TURN')
            sleep(1)
            if len(match_table) == 2:
                a = 2
            elif len(match_table) == 1:
                a = 1
            else:
                a = randint(1, 3)
        print(match_table[:-a])
        print('Removed {}'.format(a))
        print('-------------------------------------------------------\n')
        match_table = match_table[:-a]
        if len(match_table) > 0:
            print('Current number of matches on the table: {}'.format(len(match_table)))
        if i % 2 == 0 and len(match_table) == 0:
            print('CONGRATULATIONS!!!! YOU WIN :)')
        elif i % 2 == 1 and len(match_table) == 0:
            print('YOU LOSE :(')
        i += 1


matches_game()
