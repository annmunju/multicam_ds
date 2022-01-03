
def input_member(fileName_w):
    f = open(fileName_w, 'w')
    writeName = input('멤버를 입력하세요. (종료는 q) : ')
    while True:
        f.write(writeName)
        writeName = input('멤버를 입력하세요. (종료는 q) : ')
        if writeName == 'q':
            break
        f.write('\n')

def output_member(fileName_r):
    f = open(fileName_r, 'r')
    readName = f.read()
    print(readName)

pick = input('저장 1, 출력 2, 종료 q : ')

while pick != 'q':
    if pick == '1' :
        fileName_w = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(fileName_w)
    elif pick == '2':
        fileName_r = input('멤버 명단을 저장된 파일명을 입력하세요. : ')
        output_member(fileName_r)
    pick = input('저장 1, 출력 2, 종료 q : ')
