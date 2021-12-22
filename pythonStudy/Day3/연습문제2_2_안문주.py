
# 1.

inputX = input("16진수 한 글자 입력 : ")

try :
    X = int(inputX, 16)
    print("10진수 ==> ", X)
except :
    print("16진수가 아닙니다")


# 2.

change = int(input("교환할 돈은 얼마 ? "))
m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for m in m_list:
    cnt = change // m
    change %= m
    if m != 10:
        print(f'{m}원 {cnt}장', end = ', ')
    else :
        print(f'{m}원 {cnt}장')
        print(f"바꾸지 못한 돈 ==> {change}원")



# 3.

from random import randint

numA = randint(1,6)
numB = randint(1,6)

if numA > numB :
    print(f"A의 주사위 숫자는 {numA} 입니다.")
    print(f"B의 주사위 숫자는 {numB} 입니다.")
    print('A가 이겼다.')
elif numB > numA :
    print(f"A의 주사위 숫자는 {numA} 입니다.")
    print(f"B의 주사위 숫자는 {numB} 입니다.")
    print('B가 이겼다.')
else :
    print(f"A의 주사위 숫자는 {numA} 입니다.")
    print(f"B의 주사위 숫자는 {numB} 입니다.")
    print('바겼다.')