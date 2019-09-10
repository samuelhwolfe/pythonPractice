oddNumbers = []

evenNumbers = []

divisibleByThree = []

divisibleByFour = []

divisibleByFive = []

divisibleBySix = []

divisibleBySeven = []

divisibleByEight = []

divisibleByNine = []

divisibleByTen = []

for x in range(1,101):
    if x % 2 == 0:
        evenNumbers = evenNumbers + [x]
    else:
        oddNumbers = oddNumbers + [x]

for x in evenNumbers:
    if x % 4 == 0:
        divisibleByFour.append(x)
    if x % 6 ==0:
        divisibleBySix.append(x)
    if x % 8 == 0:
        divisibleByEight.append(x)
    if x % 10 == 0:
        divisibleByTen.append(x)

for x in oddNumbers:
    if x % 3 == 0:
        divisibleByThree.append(x)
    if x % 5 == 0:
        divisibleByFive.append(x)
    if x % 7 == 0:
        divisibleBySeven.append(x)
    if x % 9 == 0:
        divisibleByNine.append(x)
        
        
