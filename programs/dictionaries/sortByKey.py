toBeSorted = {'John': 'Project Manager', 'Tim': 'Writer', 'John': 'Director',
              'Sean': 'Production Assistant', 'Fred': 'Vice President'}

def sortDictionary(dic):
    for x in sorted(dic):
        print("%s: %s" %(x, dic[x])) # The two '%s' are replaceable parameter expressions
                                     # that will be replaced by the string representations of the
                                     # values associated with those two variables.
                                     # In this case, 'x' and 'dic[x]'

sortDictionary(toBeSorted)
