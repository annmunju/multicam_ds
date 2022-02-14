'''
pw = int(input("비밀번호 입력: "))

if pw == 1234 :
    print('비밀번호가 일치합니다.')

else :
    print("비밀번호가 일치하지 않습니다.")


# 문제 : id와 password를 입력받아 모두 다 맞으면 로그인 성공

id = input("아이디 입력: ")
pw = int(input("비밀번호 입력: "))

if id == 'multicampus' and pw == 1234 :
    print('로그인 성공')
else :
    print('로그인 실패')

# 문제 : 정수를 입력받아서 홀수인지 짝수인지 판별하여 출력

num = int(input("정수 입력:"))

if num % 2 == 0 :
    print('짝수')
else :
    print('홀수')

'''

# 문제 : 점수를 입력받아서 학점 출력 (A~D,F)


score = int(input("점수 입력: "))

if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")