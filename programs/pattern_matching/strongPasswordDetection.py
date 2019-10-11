#! python3

# strongPasswordDetection.py
# a simple function to test whether a password is 'strong'

import re

def strongPassword(password):
    passwordRejex = re.compile(r'''(
        .{8,}        # 8 or more characters
        \d+
        [a-z]+
        
        )''', re.VERBOSE)
    strong = passwordRejex.search(password)
    
    if strong == None:
        print('Invalid password')
    else:
        print('Password saved: ' + str(strong))

strongPassword(input('Please type a password: '))

