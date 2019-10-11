#! python3

# strongPasswordDetection.py
# a simple function to test whether a password is 'strong'

import re

def strongPassword(password):
    strong = 0
    while True:
        if (len(password) < 8):
            strong = -1
            break
        elif re.search(r'\s', password):
            strong = -1
            print('No spaces allowed.')
            break
        elif not re.search("[a-z]", password):
            strong = -1
            break
        elif not re.search("[A-Z]", password):
            strong = -1
            break
        elif not re.search("[0-9]", password):
            strong = -1
            break
        elif not re.search("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
            strong = -1
            break
        else:
            strong = 0
            print('Password saved.')
            break
    if strong == -1:
        strongPassword(input('Password invalid. Try again: '))



strongPassword(input('Please type a password: '))

