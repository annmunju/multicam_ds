# i = 1
#
# while i <= 10:
#     print(i, end = ' ')
#     i += 1

# input_num = input('숫자를 입력하세요: ')
# num_cnt = 0
#
# while input_num != 'stop':
#     input_num = input('숫자를 입력하세요: ')
#
#     try :
#         num = int(input_num)
#         num_cnt += 1
#     except :
#         continue
#
#
# print(f'숫자 갯수 : {num_cnt}')


# 7 입력할 때 까지 계속 입력하기

# num = int(input("숫자 입력 : "))
#
# while num != 7:
#     num = int(input("숫자 입력 : "))
#
# print('7 입력! 종료')

while True :
    num = int(input("숫자 입력 : "))
    if num == 7:
        break
print('7 입력! 종료')