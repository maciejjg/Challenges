#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Program that will download trade names of angular grinder tools from the www.ceneo.pl
"""

import urllib.request
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def all_urls():
    list_of_urls = []
    for number in range(1, 52):
        list_of_urls.append('https://www.ceneo.pl/;szukaj-szlifierka+katowa;0020-30-0-0-' + str(number) + '.htm')
    return list_of_urls


def foo(url):
    f = urllib.request.Request(url)
    response = urllib.request.urlopen(f)
    data = response.read()
    soup = BeautifulSoup(data, 'lxml')
    text_find_list = soup.findAll('img')

    list_of_tools = []
    for elem in text_find_list:
        if elem.get('alt', '') not in list_of_tools and elem.get('alt', '') != '':
            list_of_tools.append(elem.get('alt', ''))
    return list_of_tools


for i in all_urls():
    print(foo(i))