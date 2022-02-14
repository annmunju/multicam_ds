# abs() : 절대값 계산
print(abs(-1234))

# all() : 모든 요소가 참이면 True
print(all([-1,1,3,2])) # 0은 False

# iterable 반복가능한 자료형

# any() : 하나라도 참이면 True
print(any([0, False, [], '']))

# bool() : 불리언 값으로 변환

# chr() : 아스키코드에 해당하는 문자 반환
print(chr(100))
print(chr(1000))

# ord() : 문자에 해당하는 아스키코드 반환
print(ord('a'))
print(ord('1'))

# divmod(a, b) : a를 b로 나눈 몫과 나머지 반환
print(divmod(100,3))

# enumerate() : 시퀀스(range, 문자열, 리스트, 튜플)를 인덱스 값에 포함해서
for i, c in enumerate('hello'):
    print(f'index = {i}, text = {c}')

# eval(표현식) : 표현식의 연산 결과 반환
print(eval('234*12-36//12**2'))

# filter(정의한 함수, iterable) : 이터러블한 객체들을 함수에 삽입해보고 해당 값만 반환.
def positive(x):
    return x>0

[print(i, end=' ') for i in filter(positive, (0, 1, -1, 10, -3, 5))]

print()

# help() : 도움말
help(input)

# pow(x,y) : x의 y제곱
print(pow(10,3))

# range(시작, 끝, 단계) : 지정 범위 값을 반복 가능한 객체로 반환

# map() 함수 : iterable한 구조의 요소별로 지정된 함수를 적용하여 반환(리스트, 튜플형식으로)
# list(map(함수, 리스트)), tuple(map(함수, 튜플))

# ls = list(map(int, input().split()))
# print(ls)

# 문제
number1 = [3.5, 3.4, 2.0, 4.6]

# map을 이용하는 경우
numLs1 = list(map(int, number1))
print(numLs1)

# for을 이용하는 경우
numLs2 = []
for i in number1:
    numLs2.append(i)
print(numLs2)

# for i,n in enumerate(number1):
#     number1[i] = int(n)
# print(number1)

# zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(list(zip([1,2,3],[4,5,6]))) # 튜플형태로 묶여짐
print(dict(zip([1,2,3],[4,5,6]))) # 딕셔너리형태로 묶여짐