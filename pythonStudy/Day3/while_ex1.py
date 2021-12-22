# # while문 무한루프 이용
#
# inputA = input("입력: ")
# while True:
#     if inputA == 'q':
#         print('입력 종료!')
#         break
#     inputA = input("입력: ")

# while문 continue 이용

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end = ' ')
    i += 1
    else :
        i += 1
        continue
