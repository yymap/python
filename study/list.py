def listToStr(listObj) :
    size = len(listObj)
    ret = ''
    if size == 0 :
        return ret

    ret = str(listObj[0])
    if size == 1 :
        return str(ret)
    
    for i in range(1,size-1) :
        ret = ret + ',' + str(listObj[i])

    ret = ret + ' and ' + str(listObj[size-1])

    return ret

def testListToStr(listObj) :
    print('list one:', end = ' ')
    print(listObj)
    ret = listToStr(listObj)
    print('Convert to str :' + ret)


testListToStr([])
testListToStr([1])
testListToStr((1,))
testListToStr([1,2,3])
testListToStr(['hello','111','is', 1,2,3])
