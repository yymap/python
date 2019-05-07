import pprint
def charCount(msg) :
    count = {}
    for ch in msg :
        count.setdefault(ch,0)
        count[ch] = count[ch] + 1

    return count


def testCharCount() :
    count = charCount('Heloo, this is a test for dic')
    print(count)
    print('*******************************')
    pprint.pprint(count)
    print('*********************************')
    val1 = pprint.pformat(count)
    print(val1)

# testCharCount()


# tictactoe begin
def printBoard(bd) :
    print(bd['TL'] + '|' + bd['TM'] + '|' + bd['TR'] )
    print('-+-+-')
    print(bd['ML'] + '|' + bd['MM'] + '|' + bd['MR'] )
    print('-+-+-')
    print(bd['LL'] + '|' + bd['LM'] + '|' + bd['LR'] )
    print('-+-+-')

def getWinnerCore(s) :
    if s == 'OOO' :
        return 'O'
    elif s == 'XXX' :
        return 'X'
    return ''

def getWinner(bd) :
    ret = getWinnerCore(bd['TL'] + bd['TM'] + bd['TR'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['ML'] + bd['MM'] + bd['MR'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['LL'] + bd['LM'] + bd['LR'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['TL'] + bd['ML'] + bd['LL'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['TM'] + bd['MM'] + bd['LM'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['TR'] + bd['MR'] + bd['LR'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['TL'] + bd['MM'] + bd['LR'])
    if ret != '' :
        return ret

    ret = getWinnerCore(bd['LL'] + bd['MM'] + bd['TR'])
    if ret != '' :
        return ret

    return ''

    

def tictactoe() :
    board = {"TL" : ' ','TM' : ' ', 'TR' : ' ',
             'ML' : ' ','MM' : ' ', 'MR' : ' ',
             'LL' : ' ','LM' : ' ', 'LR' : ' '}
    turn = ''
    for i in range(len(board)) :
        printBoard(board)
        if getWinner(board) != '' :
            print(turn + ' has win!')
            break
        
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        while board.get(move,' ') != ' ' :
            print('The space has been used, move another:')
            move = input()
        if turn == 'X' :
            turn = 'O'
        else :
            turn = 'X'
        board[move] = turn

tictactoe()
        
            
