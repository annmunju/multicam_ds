# 개선된 선택정렬 구현

import random

def selectionSort(ary):
    n = len(ary) # 데이터 개수
    for cy in range(n-1):
        minIdx = cy
        for i in range(cy+1, n):
            if ary[minIdx] > ary[i]:
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary

dataAry = [random.randint(0,99) for _ in range(20)]

print('정렬 전 :',dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 :',dataAry)
