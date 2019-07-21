import pyperclip
import re

rawinput = pyperclip.paste()

emailRegex = re.compile(r'''(
                        [A-Za-z0-9-+._%]+   # username
                        @                   # @ symbol
                        [A-Za-z0-9.-]+      # Email hoster
                        (\.[a-zA-Z]{2,4})   # Domain name
                        (\.[a-zA-Z]{2,4})?  # Optional multiples
                        )''', re.VERBOSE)

# This specifically for UK phone numbers
phoneRegex = re.compile(r'''(
                        [+\d\d\d?]? # Country address?
                        \s?        # Possible space?
                        0?         # possible 0?
                        [0-9]{4}   # Area code
                        \s?        # Maybe a space?
                        [0-9]{6}   # Second part (localised)
                        )''', re.VERBOSE)

mo = emailRegex.findall(rawinput)
mo1 = phoneRegex.findall(rawinput)

for group in range(len(mo)):
    print(mo[group][0])

for group in range(len(mo1)):
    print(mo1[group])

print(mo)
print(mo1)
