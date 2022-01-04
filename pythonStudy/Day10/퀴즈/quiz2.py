# 2. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# 한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기

def sum(readFile, writeFile):
    fr = open(readFile, 'r')

    num_ls = []
    lines = fr.readlines()
    for line in lines:
        num_str = line.split()
        if not num_str :
            continue
        num_int = list(map(float, num_str))
        num_ls.append(num_int)

    fw = open(writeFile, 'w')
    for num in num_ls :
        fw.write(f'{num[0]}+{num[1]}={num[0]+num[1]}\n')

    fr.close()
    fw.close()

sum('list_num.txt', 'culc_num.txt')
