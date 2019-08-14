#! python3

import shelve
import pyperclip
import sys

usage = """
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.py save <keyword> - Saves clipboard to keyword.
#        py mcb.py delete <keyword> - deletes keyword
#        py mcb.py <keyword> - Loads keyword to clipboard.
#        py mcb.py list - Loads all keywords to clipboard.
#        py mcb.py clear - clears the whole multiclipboard
#        py mcb.py help - shows usage"""

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Deletes specific clipboard content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
# Deletes all clipboard content
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'clear':
    for key in list(mcbShelf.keys()):
        del mcbShelf[key]
# Display usage
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'help':
    print(usage)
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        for keyword in list(mcbShelf.keys()):
            print(keyword)
    # If the keyword exists, copy to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ' found, copied to clipboard')
    else:
        print(usage)
else:
    print(usage)
mcbShelf.close()
