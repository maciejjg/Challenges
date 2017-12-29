#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Sergeant Thomson decided to censor the mail of his polish soldiers. 
From each letter he censors every third line and additionally he censors every line containing the polish word "kocham" (regardless of the case of the letters). 
Help sergeant Thomson in this task. Write a program that reads a letter from a file and writes its censored version. Censored lines should be replaced by the sequence
"""
import os

def lines_to_censore(file, find_word):
    lines_kocham = []
    number = 0
    with open(file, 'r') as text_file:
        lines = text_file.read().split('\n')
        lx = [[l.lower()] for l in lines]
        for row in lx:
            number += 1
            for r in row:
                if find_word in r or number % 3 == 0:
                    lines_kocham.append(number)
        return lines_kocham


def censore_me(file):
    new_list = []
    line_number = 0
    with open(file, 'r') as text_file:
        for lines in text_file:
            line = lines.split('\n')
            new_list.append(line[0])
        new_file = open('Censored.txt', 'w')
        for i in new_list:
            line_number += 1
            if line_number in lines_to_censore(file, "kocham"):
                i = '*****\n'
            else:
                i = i + '\n'

            new_file.write(i)
        new_file.close()


censore_me("Test123.txt") # at this place put name of input file that has to be censored
print('The file was created in directory: \n' + os.path.abspath("Censored.txt"))




