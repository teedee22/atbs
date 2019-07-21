# Regular expression for strong password protection
import re

password = input("Enter password: ")

passRegex = re.compile(r'''(
                      ([a-z]+[A-Z]+){8,}
                      )''', re.VERBOSE)

mo = passRegex.search(password)

print(mo)
