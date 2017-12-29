#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Create a table of multiplication 100x100 in the CSV format. Open it in Excel.
"""

import csv
import os

def multiplication_tables(size):
    multiplication_list = list(list(range(1 * i, (size + 1) * i, i)) for i in range(1, size + 1))
    return multiplication_list


def save_to_csvFile(file):
    with open("MultiplicationTable.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        [writer.writerow(r) for r in file]


save_to_csvFile(file=multiplication_tables(100))


print('The file was created in directory: \n' + os.path.abspath("MultiplicationTable.csv"))