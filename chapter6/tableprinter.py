# Practice project - table printer http://automatetheboringstuff.com/chapter6/

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colNo = 0
    maxLength =0
    # Count the number of columns

    for i in range(len(tableData[0])):
        colNo += 1
    # Find the maximum word length

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if maxLength < len(tableData[i][j]):
                maxLength = len(tableData[i][j])

    # Print the table to the terminal
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(maxLength+3, ' '), end='')
        print()


printTable(tableData)
