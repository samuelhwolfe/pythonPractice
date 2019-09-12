playerInventory = {'rope': 1, 'torch': 6, 'dagger': 2, 'gold coin': 50,
                   'arrow': 10}

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        individual_item = k + ": " + str(v)
        print(individual_item, end='\n')
        item_total = item_total + inventory.get(k, 0)
    print('Total number of items: ' + str(item_total))

displayInventory(playerInventory)
