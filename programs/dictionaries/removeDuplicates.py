myList = {'Samuel': 'Manager', 'Samuel': 'Assistant', 'Tim': 'Writer',
          'John': 'Accountant'}

def removeDuplicates(dic):
    for key in dic.keys():
        if key > 1:
            dic.pop(key)
        print(str(dic))

removeDuplicates(myList)
    
