userInputs = []

while len(userInputs) < 10:
    x = int(input('Type an integer: '))
    userInputs = userInputs + [x]
    print('The average of your inputs is: ' + str(sum(userInputs)/len(userInputs)))

   
    




