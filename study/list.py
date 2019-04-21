def listToStr(listObj,sep=',',end='and') :
    size = len(listObj)
    ret = ''
    if size == 0 :
        return ret

    ret = str(listObj[0])
    if size == 1 :
        return str(ret)
    
    for i in range(1,size-1) :
        ret = ret + sep + str(listObj[i])

    ret = ret + end  + str(listObj[size-1])

    return ret

def testListToStr(listObj,sep=',',end='and') :
    print('list one:', end = ' ')
    print(listObj)
    ret = listToStr(listObj,sep,end)
    print('Convert to str :' + ret)


testListToStr([])
testListToStr([1])
testListToStr((1,))
testListToStr([1,2,3],sep='',end='')
testListToStr(['hello','111','is', 1,2,3])
