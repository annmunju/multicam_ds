# 1. 1)
for i in range(5,0,-1):
    print("*"*i)

# 1. 2)
n = 4
for i in range(1,10,2):
    print(' '*n,'*'*i)
    n -= 1

# 2.
num = int(input('숫자 입력 : '))
while num != 7:
    num = int(input('다시 입력 : '))
print('7 입력! 종료')

# 3.
sing = 1
change = 10000 - 2000
print(f'노래를 {sing}곡 불렀습니다.\n현재 {change}원 남았습니다.')

while change != 0:
    sing += 1
    change -= 2000
    print(f'노래를 {sing}곡 불렀습니다.\n현재 {change}원 남았습니다.')

print("잔액이 없습니다. 종료합니다.")