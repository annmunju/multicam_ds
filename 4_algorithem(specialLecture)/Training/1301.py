# 순차 검색

import random

def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)
    for i in range(size):
        if ary[i] == fData:
            pos = i
    return pos


SIZE = 10
dataAry = [random.randint(1,99) for _ in range(SIZE)]
findData = dataAry[random.randint(0, SIZE-1)]

print('배열 :', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없음')
else :
    print(findData,'가 ',position,'에 있음')