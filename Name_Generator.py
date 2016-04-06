# Name generator

import random

girl_names = [
    'Miranda', 'Alice',
    'Britney', 'Monica'
]

men_names = [
    'Tom', 'Bob',
    'Henry', 'Johny'
]


def foo():
    if your_choice == 'f':
        result = random.choice(girl_names)
        print(result)

    elif your_choice == 'm':
        result = random.choice(men_names)
        print(result)
    elif your_choice == 'r':
        new_list = girl_names + men_names
        result = random.choice(new_list)
        print(result)

your_choice = input("NAME GENERATOR \nfemale (choose f) \nmale (choose m) \nI do not care (choose r): ").lower()

if len(your_choice) > 1:
    print('You entered more than one character')

while your_choice.isalpha():
    foo()
    break
else:
    print('You entered the illegal character which is a number')


