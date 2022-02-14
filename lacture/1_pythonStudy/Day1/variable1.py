# 2021-12-20 변수
# 변수의 특징
# 1) 값(객체)이 저장된 메모리의 위치를 가리키는 레퍼런스
# 2) 값의 형에 따라서 고정되지 않고, 동적으로 자료형을 검사함 : type 검사
# 3) 변수는 이름을 가지고 있다. 변수 값을 변경할 수 있다. 변수선언(형 지정)은 필요 없다.

x = 10
print(x)

y='hello'
print(y)
y='haha'
print(y)
y=10.5
print(y)

z=[10,30,40]

id(z) # 변수가 가리키는 값(객체)의 주소
type(z) # 변수가 가리키는 값의 형식


# 변수 이름 지정 규칙 (명명규칙)
# 1) 대소문자 구분(C언어 기반)
# 2) 영문자, 숫자, 밑줄 사용 가능
# 3) 중간에 공백이 오면 안묃. _(snake)나 중간에 대문자(camel)를 사용해서 구분.
# 4) 예약어는 변수명으로 사용 불가
#   ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
#   'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
#   'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#   'raise', 'return', 'try', 'while', 'with', 'yield']

# 이외의 변수 선언 방법
# 1) a, b, c = 1, 2, 3
# 2) a = b = c = 100

# 변수 제거 : del 변수명

# 형변환 : str(  ), float(   ), int(   )

# 문제 : 자신의 이름과 나이를 변수에 저장 후 print()를 이용해 한 줄에 출력
name = '안문주' ; age = 25 ; print('저는 '+name+'입니다. 나이는 '+str(age)+'살 입니다.')

# 문제 2
name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5

print(f'성명 : {name} \n학번 : {no} \n학년 : {year} \n학점 : {grade}\n평균 : {average}')


# ---

# formating : print()에서 문자열과 변수를 함께 출력하고자 할때
# 1) print("%d %s %f" % 변수)
# 2) print('{}'.format(변수))
# 3) print(f'{변수}')