humans = {'Samuel': 'human', 'Veronika': 'human', 'Ellis': 'human'}
dogs = {'Murphy': 'dog', 'Kona': 'dog'}

def merge(dic1, dic2):

    newList = {}
    for x in (dic1, dic2):
        newList.update(x)
    print(newList)

merge(humans, dogs)
    
