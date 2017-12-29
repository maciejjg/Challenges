#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def date_form():
    user_data = {}
    name = input("Name: ")
    surname = input("Surname: ")
    city = input("City: ")
    phone = input("Phone: ")
    zip_code = input("Postal code: ")

    regex_name = r'^(\b[A-Z]\w*\s*)+$'
    regex_surname_city = r'^(\b[A-Z-]\w*\s*)+$'
    regex_zip_code = r'^[0-9]{2}-[0-9]{3}$'
    regex_phone = r'^[(][0-9]{2}[)][ ][0-9]{3}[-][0-9]{2}[-][0-9]{2}$'

    check_name = re.search(regex_name, name)
    check_surname = re.search(regex_surname_city, surname)
    check_city = re.search(regex_surname_city, city)
    check_phone = re.search(regex_phone, phone)
    check_zip_code = re.search(regex_zip_code, zip_code)

    if check_name != None:
        print('Name correct validated')
        user_data.update({'name': name})
    else:
        print('Error! First character of name must be large')

    if check_surname != None:
        print('Surname correct validated')
        user_data.update({'surname': surname})
    else:
        print('Error! First character of surname must be large')

    if check_city != None:
        print('City correct validated')
        user_data.update({'city': city})
    else:
        print('Error! First character of city name must be large')

    if check_phone != None:
        print('Phone correct validated')
        user_data.update({'phone': phone})
    else:
        print('Error! Phone must has format like (61) 222-45-56')

    if check_zip_code != None:
        print('Postal code correct validated')
        user_data.update({'zipcode:': zip_code})
    else:
        print('Error! Postal code must has format like 11-111')
    print('\n\nCurrent client data:')
    print(user_data)

date_form()
