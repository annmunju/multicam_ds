# with문이 종료되면 파일객체는 자동으로 close()
# with open(파일명, 모드) as 파일 객체 :

with open('file2.txt', 'r') as f:
    print(f.read())

file = 'file1.txt'
data = 'Python programming'

with open(file, 'a') as f:
    f.write('\n'+data)