groceries = ['bananas', 'carrots', 'strawberries']
supplies = ['pens', 'paper', 'markers']

def mergeLists(list1, list2):
    
    merge_lists = dict(zip(list1, list2))
    print(merge_lists)

mergeLists(groceries, supplies)
    
