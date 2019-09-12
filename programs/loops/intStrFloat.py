comboList = [5, 2, 3, 5, 11, 37, 98, 99, 101, 44, 5.0, 2.4, 3.0, 88.9, Kona, Murphy, Ellis, Veronika]

intList = []

strList = []

floatList = []
    

for x in comboList:
    if type(x) == int:
        intList = intList + [x]
    if type(x) == float:
        floatList = floatList + [x]
    else:
        strList = strList + str([x])

print(intList)
print(floatList)
print(strList)
