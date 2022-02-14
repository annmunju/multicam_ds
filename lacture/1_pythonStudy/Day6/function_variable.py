# 지역변수와 전역변수

def show(b):
    global a
    a = 1
    a = a + b
    print('show() 함수')
    print(a)

show(100)
print(a)
