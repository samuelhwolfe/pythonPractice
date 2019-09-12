sampleDictionary = {'Arri': 5, 'RED': 6, 'Sony': 4}

def keyInDictionary(key):
    if key in sampleDictionary:
        print('That key is in the dictionary.')
    else:
        print('That key is not in the dictionary.')

x = input('Type a key to see if it is in Dictionary: ')

keyInDictionary(x)
