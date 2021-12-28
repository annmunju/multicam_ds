# def 함수명 (매개변수1, 매개변수2) :
#   수행 문장 1
#   수행 문장 2
#   반환값(생략 가능) return

# 변수는 괄호가 없고, 함수는 괄호가 있다.
# 함수 이름은 소문자 사용 권장

# 함수명() 매개변수 없이 하면 호출시에 함수명()로 불러올 수 있음.

def show_info():
    print('이름 : 안문주')
    print('나이 : 25')

show_info()

def welcome(n):
    for _ in range(n):
        print('welcome!')

welcome(3)

# 두개 숫자 입력받아 합을 구하여 출력하는 함수 작성

def sumnum():
    num1 = int(input('숫자1 입력 : '))
    num2 = int(input('숫자2 입력 : '))
    return num1 + num2

print('합 :',sumnum())