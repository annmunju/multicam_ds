# 문제 1

positive = 0
negative = 0
zero = 0

for i in range(1,11):
    num = int(input(f'숫자{i}입력 : '))

    if num > 0 :
        positive += 1
    elif num < 0 :
        negative += 1
    else :
        zero += 1

print('-'*30)

print(f"양의 개수 : {positive}")
print(f"음의 개수 : {negative}")
print(f"0의 개수 : {zero}")

# 문제 2

names = ['베토벤', '홍길동', '변학도', '아쿠아맨']
search_name = input('이름 입력 : ')

for n in names:
    if n == search_name:
        find = True
        break
    else :
        find = False

if find :
    print('명단에 있네요')
else :
    print('명단에 없네요')