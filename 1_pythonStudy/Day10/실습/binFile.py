# open('이진파일 이름', 'rb')
# read(1) #1 바이트씩 읽기
# open('이진파일 이름', 'wb')
# write() # 이진파일 쓰기

# exe 파일 읽기 (.,.?)

f1 = open('/Users/anmunju/Downloads/pycharm.dmg', 'rb')
f2 = open('/Users/anmunju/Downloads/new/pycharm.dmg', 'wb')

while True :
    inStr = f1.read(1)
    if not inStr:
        break
    f2.write(inStr)

f1.close()
f2.close()