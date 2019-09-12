shoppingList = {'Apples': 5, 'Bananas': 4, 'Blueberries': 3,
                'Wine': 3, 'Potatoes': 6, 'Bread': 4}


def removeKey(key, dic):
    if key in dic.keys():
        dic.pop(key)
    print(dic)


print(shoppingList)

searchItem = input('Enter an item to remove it from the list: ')

removeKey(searchItem, shoppingList)
        
