# isalpha() 문자 여부 결과 반환 (T, F)
# isdigit() 숫자
# isspace() 공백여부
# isalnum() 문자 또는 숫자인지
# islower() isupper

# string = '내 이름은 mjAhn 이고 나이는 25 입니다.'
# str_split = string.split()
# for result in str_split:
#     if result.isdigit():
#         age = result
# print(f'나이는 {age}세')


# 문제 : 입력된 문자열에서 알파벳 숫자 스페이스 기타의 개수를 각각 계산해서 출력하기


inputX = input("문장을 입력하세요 : ")

alp = num = space = etc = 0

for i in inputX:
    if i.isalpha() == True :
        alp += 1
    elif i.isdigit() == True :
        num += 1
    elif i.isspace() == True :
        space += 1
    else :
        etc += 1

print(f'알파벳 개수:{alp}, 숫자 개수:{num}, 스페이스 개수:{space}, 기타 개수:{etc}')