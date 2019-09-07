#for i in range(5):
#    for x in range(5-i):
#        print("X",end='')
#    print()

userList = []

while True:
    
    print('\nType some inputs: \n')
    
    name = input()
    
    if name == '':
        for x in userList:
            
            userSearch = input('Type an input to see if it\'s in the list.')

            if userSearch in userList:
                yesOrNo = input('\nYes, that value is in the list. Do you want to delete it? ')
                
                if yesOrNo in ['Yes', 'yes']:
                    userList.remove(userSearch)
                    print('\nOkay that value has been deleted. Your list now contains: \n\n' + str(userList))
                    
                else:
                    break
                   
            else:
                yesOrNo = input('\nNo, that value is not in the list. Do you want to add it to the list? ')
                
                if yesOrNo in ['Yes', 'yes']:
                    userList.append(userSearch)
                    break
                
                elif yesOrNo in ['No', 'no']:
                    break
                
    userList = userList + [name]


    
    
        

