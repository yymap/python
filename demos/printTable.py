#! python3
def printTable(content) :
    listCount = len(content)
    colWidth = [0] * listCount
    rowCount = 0
    print('The raw list is :')
    for i in range(listCount) :
        print(' '.join(content[i]))
        if rowCount < len(content[i]) :
            rowCount = len(content[i])
            
        for s in content[i] :
            if colWidth[i] < len(s) :
                colWidth[i] = len(s)

    print('Row count is ' + str(rowCount))

    rows = [''] * rowCount
    for i in range(rowCount) :
        for j in range(len(colWidth)) :
            rows[i] = rows[i] + content[j][i].rjust(colWidth[j]) + ' '

    return'\n'.join(rows)
    

def testPrintTable() :
    table = [['aa','bbb','ddd'],
             ['cccc','dddd','f'],
             ['kkkkkkk','d','ddddfff']]
    print(printTable(table))


    
testPrintTable()
