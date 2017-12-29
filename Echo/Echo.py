#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Program that read a text file line by line.
Each line should be brought to lowercase and the last 5 letters of the line should be repeated.
Write the modified lines.
"""

def echo_text_reader(file):
    with open(file, 'r') as text_file:
        lines = text_file.read().split('\n')
        lx = [[l.lower()] for l in lines]

        for line in lx:
            print(''.join(line), line[0][-5:], sep='')


echo_text_reader("text_for_echo.txt") # at this place put file txt to repeated echo
