#!/bin/python3
from core import Make
import config
import os


# get the link from user
while True:
    link = input('insert link which you want to shorten: ')
    if link:
        break
    else:
        print('fetal: url should not be blank')

# take a name for shorted url from user
name = input('short name for url(or just pass it blank to random): ')

# chose user should click to open the link or just redirect it
while True:
    click = input('make user click to open the link(y/n)?: ')
    if click == 'y':
        click = True
        break
    elif click == 'n':
        click = False
        break
    else:
        print('fetal: enter y for yes, and n for no')

# the title for individual link page
title = input('type the title: ')

# any desctiption for individual link page
description = input('describe sotmething before redirection: ')

# copy style dependency
with open(os.path.join(config.DIR, 'style.css'), 'r') as rstyle:
    with open(os.path.join(config.PUBLISH_DIR, 'style.css'), 'w') as wstyle:
        wstyle.write(rstyle.read())

# generate the page
link = Make(link=link, title=title, desc=description, click=click, name=name)
print(os.path.join(config.BASE_URL, os.path.split(link)[1]))
