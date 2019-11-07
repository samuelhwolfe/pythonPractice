#! python 3
# sentenceMatching.py - matches sentences according to set parameters

import re

def sentenceMatch(sentence):

    sentenceRegex = re.compile(r'''(
        (Alice|Bob|Carol)\s             # must end with a period
        (eats|pets|throws)\s            # second word with a space at the end
        (apples|cats|baseballs)\.       # third word with period at the end
        )''',re.I | re.VERBOSE)

    match = sentenceRegex.search(sentence)

    while True:
        if match == None:
            print(sentenceMatch(input('No match. Please try again: ')))
            break
        else:
            print('Match found: ' + match.group())
            break

sentenceMatch(input('Type a sentence to find a match: '))

s
