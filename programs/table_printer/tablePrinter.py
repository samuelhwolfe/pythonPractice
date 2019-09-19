tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(inputList):

        colWidths = [0] * len(inputList)

        for x in range(len(inputList)):
            for y in range(len(inputList[x])):
                if len(inputList[x][y]) > colWidths[x]:
                    colWidths[x] = len(inputList[x][y])

        for i in range(len(inputList[0])):
            for j in range(len(inputList)):
                print(inputList[j][i].rjust(colWidths[j]),end =' ')
            print()
            
    

        
printTable(tableData)

