# Regular expression for strong password protection
import re
import sys


if len(sys.argv) != 2:
    print("Usage: Enter one password as argument")
else:
    password = sys.argv[1]

    passCaps = re.compile(r'[A-Z]')
    passLower = re.compile(r'[a-z]')
    passNums = re.compile(r'[0-9]')

    caps = passCaps.search(password)
    lower = passLower.search(password)
    num = passNums.search(password)

    if not caps:
        print("You need at least one capital letter")
    if not lower:
        print("You need at least one lowercase letter")
    if not num:
        print("You need at least one number")
    if not len(password) >= 8:
        print("You need at least 8 characters")
    if caps and lower and num:
        if len(password) >= 8:
            print("password secure")
