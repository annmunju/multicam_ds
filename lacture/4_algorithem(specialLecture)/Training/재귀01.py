from typing import Counter


def openBox():
    global count
    print('종이 상자 열기~', count)
    count -= 1
    if count == 0:
        print('** 반지 넣기 **')
        return
    openBox()
    print('종이 상자 닫기!', count)
    return

count = 3

openBox()