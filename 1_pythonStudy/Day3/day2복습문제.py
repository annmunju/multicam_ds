
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

max = num1

if num2 > max :
    max = num2
if num3 > max :
    max = num3

print('제일 큰 수 : %d' % max)


# ---

fig = int(input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : "))
result = 0

if fig == 1:
    figName = "사각형"
    width = int(input("가로 입력 : "))
    leng = int(input("세로 입력 : "))
    result = width * leng
elif fig == 2:
    figName = "삼각형"
    base = int(input("밑변 입력 : "))
    height = int(input("높이 입력 : "))
    result = base * height / 2
elif fig == 3:
    figName = "원"
    radius = int(input("반지름 입력 : "))
    pie = 3.141592
    result = pie * radius ** 2
else :
    pass

if result == 0 :
    print('잘못 입력했습니다.')
else :
    print('%s의 면적 = %.2f' % (figName, result))