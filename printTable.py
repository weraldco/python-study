
testTable = [
    ['Rodrigo', 'Taylor', 'Ariana', 'Harlse','Jenny'],
    ['black', 'red', 'orange', 'violet','green'],
    ['siomai', 'siopao','shawarma'] 
]

def checkTableSize(tables):
    hashmap = {}
    higher = {}
    for i, item in enumerate(tables):
        size = len(item)
        hashmap[i] = size

        if len(hashmap) != 1:
            if hashmap[i] >= higher['h']:
                higher['h'] = hashmap[i]
        else:
            higher['h'] = hashmap[i]
        
    for i in range(len(tables)):
        while len(tables[i]) != higher['h']:
            tables[i].append('no-data')
     
    return higher['h']


def printTable(tables):

    tsize = checkTableSize(testTable)

    cols = tsize
    rows = len(tables)
    newTable = []

    for i in range(len(tables)): #3.
        while len(tables[i]) == tsize:
            tables[i].append('-')

    for c in range(cols):
        test = [tables[r][c] for r in range(rows)] 
        newTable.append(' '.join(test))

    return '\n'.join(newTable)

print (printTable(testTable))
