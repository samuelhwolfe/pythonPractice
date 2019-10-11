#! python3
# findNakamoto.py - matches names with the last name Nakamoto

import re

def findNakamoto(name):

    nakamotoRegex = re.compile(r'''(
        ([A-Z]){1}
        ([a-z])+\s
        ([Nakamoto]){8}
        )''', re.VERBOSE)

    while True:
        match = nakamotoRegex.search(name)
        if match == None:
            break
        else:
            print('Match found: ' + match.group())
            break
    print(findNakamoto(input('No match found. Please try again: ')))

findNakamoto(input('Type in a name: '))
