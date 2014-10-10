# -*- coding: utf-8 -*-
import re
import hashlib
from datetime import date


def get_username(name, mail):
    username = name.strip()
    if len(username) > 30:
        if len(mail) > 30:
            username = mail[0:mail.index('@')]
            if len(username) > 30:
                h = hashlib.md5()
                h.update(username)
                username = h.digest()
        else:
            username = mail
    return username


def get_title(sekso):
    if sekso == 'Ina':
        return 'Mrs'
    if sekso == 'Vira':
        return 'Mr'
    return ''


def get_birth_date(year):
    if year:
        year = year.strip(' .-')
        if len(year) == 4:
            return date(int(year), 1, 1)
        if len(year) == 2 and int(year) > 30:
            return date(int('19'+year), 1, 1)
        if '/' in year:
            day, month, y = year.split('/')
            if len(y) == 2:
                return date(int('19'+y), int(month), int(day))
            elif len(y) == 4:
                return date(int(y), int(month), int(day))
        else:
            print('Invalid birth year:', year)
    return None


def get_postcode(string):
    postcode = string.strip()
    if len(postcode) > 11:
        if ' TX, ' in postcode:
            # Just for one postcode, cutting the begining where is 4 digit house number
            postcode = postcode[5:]
        matches = re.search(r'([0-9\-]{4,11})', postcode)
        if matches:
            postcode = matches.group()
        else:
            print('Invalid postcode:', postcode)
            return ''
    elif len(postcode.strip('.-')) == 0:
        return ''
    return postcode


def get_avatar(path):
    return re.sub('files/pictures/', 'avatars/', path)
