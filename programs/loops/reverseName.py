userName = input('Please type your name: ')

for letter in range(len(userName) -1, -1, -1):
    print(userName[letter], end='')
