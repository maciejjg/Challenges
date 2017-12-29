#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Program for finding all e-mail addresses in a file.
"""

import re
import urllib.request


def find_mails(url):
    list_of_emails = []
    r = urllib.request.Request(url)
    response = urllib.request.urlopen(r)
    data = response.read()

    
    finder = re.findall(r'[\w\.-]+@[\w\.-]+',str(data))
    finder_at = re.findall(r'[\w\.-]+[([]at[])][\w\.-]+', str(data))

    for email in finder:
        if email not in list_of_emails:
            list_of_emails.append(email)

    for email_at in finder_at:
        if email_at not in list_of_emails:
            list_of_emails.append(email_at)

    print(list_of_emails)


find_mails('http://') # in this place, put url from which you want to emails
