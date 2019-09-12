myInventory = {'rope': 1, 'torch': 6, 'dagger': 2, 'gold coin': 50,
                   'arrow': 10}


def displayInventory(inventory):
    print('Inventory: \n')
    item_total = 0
    for k, v in inventory.items():
        individual_item = k + ": " + str(v)
        print(individual_item, end='\n')
        item_total = item_total + inventory.get(k, 0)
    print('\nTotal number of items: ' + str(item_total))

displayInventory(myInventory)

def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return(inventory)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
