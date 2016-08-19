#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Deaw install scripts
"""

from datetime import datetime
import shutil
import sys
import os

__all__ = ['deawadmin']

def startproject():
    directory = sys.argv[2]
    if not os.path.exists(directory):
        shutil.copytree('/Users/ilogikal/Desktop/test/env/lib/python3.5/site-packages/deaw-0.0.1-py3.5.egg/deaw/source', directory)
        os.mkdir(directory + '/static')

def startapp():
    print(sys.argv[2])

def usage():
    print('Usage : ')

commands = {'startproject': startproject,
            'startapp': startapp}

def deawadmin():
    try:
        arg = sys.argv[1]
        if arg in commands:
            commands[arg]()
        else:
            usage()
    except Exception as e:
        print(e)
        usage()


if __name__ == "__main__":
    deawadmin()
