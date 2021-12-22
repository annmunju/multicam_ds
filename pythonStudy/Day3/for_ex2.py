
n = int(input('단수 입력 : '))

for i in range(1,10):
    print('{} * {} = {}'.format(n, i, n*i))



n = int(input('시작 숫자를 입력하세요 : '))

for i in range(n, 0, -1):
    print(i, end=' ')

print('성공')

score_ls = [70, 90, 100, 50, 85]
n = 0

for i in score_ls :
    n += 1
    if i >= 60:
        print('{}번 학생 합격'.format(n))
    else :
        print('{}번 학생 불합격'.format(n))