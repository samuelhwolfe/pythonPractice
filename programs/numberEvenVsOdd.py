userInput = []

oddList = []

evenList = []

while True:
    x = input('Type a series of integers: ')
    if x == '':
        break
    userInput = userInput + [x]

for x in range(0, (len(userInput))):
    userInput[x] = int(userInput[x])


for x in userInput:
    if x % 2 == 0:
        evenList = evenList + [x]
    else:
        oddList = oddList + [x]

#print(userInput)
#print(evenList)
#print(oddList)

print('You printed ' + str(len(evenList)) + ' even numbers and ' + str(len(oddList)) + ' odd numbers.')



