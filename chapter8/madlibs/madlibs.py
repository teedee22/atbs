#! /usr/bin/python3

import sys
import os
import re

usage = """usage: py madlibs.py <document>.txt"""

if len(sys.argv) == 2:
    # Search through files in the current working directory
    if sys.argv[1] in os.listdir(os.getcwd()):
        print(sys.argv[1] + ' exists')
        # Create object to read file
        readInput = open(sys.argv[1], 'r')
        # Save contents of file as a string
        contents = readInput.read()
        readInput.close()
        # split contents into a list
        contentslist = contents.split(' ')
        # compile regex
        inputregex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
        # Go through each item in the list and check it
        for i in range(len(contentslist)):
            if inputregex.search(contentslist[i]):
                mo = inputregex.search(contentslist[i])
                mo.group()
                sub = input("Enter a " + mo.group() + ":\n")
                # Substitute the word with what the user typed
                contentslist[i] = inputregex.sub(sub, contentslist[i])
        # write the output to a file
        docname = input("please provide a name for output document: ")
        writeOutput = open('%s.txt' % docname, 'w')
        writeOutput.write(' '.join(contentslist))
        writeOutput.close()
    else:
        print(sys.argv[1] + ' does not exist.')
        print(usage)
