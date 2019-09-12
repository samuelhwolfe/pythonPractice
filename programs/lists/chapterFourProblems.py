spam = ['apples', 'bananas', 'tofu', 'cats']

myFavoriteThings = ['Beer', 'Pizza', 'Family', 'Snowboarding', 'Murphy',
                    'Kona', 'Movies', 'Cheese']

def listString(myList):
    
    myList.insert(-1, 'and ')
    
    firstPortion = myList[0:-2]

    for x in firstPortion:
        print((x) + ', ', end='')
        
    lastPortion = myList[-2:]
    
    for x in lastPortion:
        print((x), end='')
    
              
myList = myFavoriteThings

listString(myFavoriteThings)







