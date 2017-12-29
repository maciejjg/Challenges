#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Program which will validate a CSV file. A valid file contains lines composed of 3 fields. 
The first field is any character sequence, second and third are integer numbers. The fields are separated by a semicolon.
"""

import re


def validator(file):
    list_of_error_lines = []
    regex = r'(?s).*[;][0-9][;][0-9]$'
    with open(file, 'r') as text_file:
        i = 0
        for lines in text_file:
            line = lines.split('\n')[0]
            checker = re.match(regex, line)
            i += 1

            if checker is None:
                list_of_error_lines.append(i)

        if len(list_of_error_lines) != 0:
            numbers_error = ', '.join(str(x) for x in list_of_error_lines)
            print('The file has errors. Errors occur on the line: {}'.format(numbers_error))
        else:
            print('CSV file is correct')


validator('example.csv') # at this place put name of your example csv file
