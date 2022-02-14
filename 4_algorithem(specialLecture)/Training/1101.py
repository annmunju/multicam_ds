import random

def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx


# testAry = [55, 88, 33, 77]
testAry = [random.randint(0,99) for _ in range(20)]

print(testAry)
minPos = findMinIndex(testAry)
print('최소값 :', testAry[minPos])
