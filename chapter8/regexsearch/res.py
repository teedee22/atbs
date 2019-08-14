#! /usr/bin/python3
import os
import re

search = input('what would you like to search for in the current directory? ')
dirSearch = re.compile(rf'{search}')

txtSearch = re.compile(r'\w*.txt')
txtlist = []
# Get a list of only .txt files in current directory
for file in os.listdir(os.getcwd()):
    if txtSearch.search(file):
        txtlist.append(file)

# Go through each of the .txt files and search for matches
for file in txtlist:
    readFile = open(file, 'r')
    filestring = readFile.read()
    matches = dirSearch.findall(filestring)
    if matches:
        for match in matches:
            print(file + ': ' + match)
