
# 한줄만 읽기
# f = open('file1.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

# 한줄씩 읽기
# f = open('file1.txt', 'r')
# while True :
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# 한번에 읽기
f = open('file1.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
for line in f: # readlines 자동 수행
    print(line, end='')
f.close()