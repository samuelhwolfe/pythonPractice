myDictionary = {0:10, 1:20}

def addToDictionary():
    
    x = int(input('Type an integer: '))
    y = int(input('Type another integer: '))
    
    myDictionary.update({x:y})
    print(myDictionary)

addToDictionary()
