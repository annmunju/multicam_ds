def countDown(n):
    if n == 0 :
        print('발사!')
    else:
        print(n)
    countDown(n-1)


def starPrint(n):
    if n > 0 :
        starPrint(n-1)
        print('*'*n)
    

def gugu(dan, num):
    print(dan,'*', num,'=', dan*num)
    if num < 9:
        gugu(dan, num+1)
        return
    num = 1
    if dan < 9:
        gugu(dan+1, num)

gugu(1,1)