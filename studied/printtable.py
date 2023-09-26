
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose'],
['red','blue','white','yellow']]

def printTable(table):
    cols = len(table[0])
    rows = len(table)

    result_list = []
    for c in range(cols):
        column = ''
        for r in range(rows):
            column += table[r][c].ljust(15)  

        result_list.append(column)
    
    return '\n'.join(result_list)
        


print(printTable(tableData))