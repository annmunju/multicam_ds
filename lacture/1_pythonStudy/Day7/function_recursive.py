# # 재귀함수
#
# # 문제1. 팩토리얼 계산
#
# def factorial(n):
#     fac = 1
#     while n != 0:
#         fac *= n
#         n -= 1
#     return fac

# # 재귀함수 활용시)
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else :
#         return n*factorial(n-1)
#
# n= int(input('숫자 입력: '))
# print(f'{n} 팩토리얼 : {factorial(n)}')

# # 문제 2. 무한으로 호출됨 > 오류!
#
# def selfCall():
#     print('hello', end=' ')
#     selfCall()
#
# selfCall()

# 문제 3. 숫자 카운트 함수

# 반복문 이용
def count1(number):
    for i in range(number, 0, -1):
        print(i)

# 재귀함수 이용
def count2(number):
    if number == 1 :
        return print(1)
    else :
        print(number)
        return count2(number-1)

count1(5)
count2(5)