# 2. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# 한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기

fr = open('list_num.txt', 'r')
num_ls = []
lines = fr.readlines()
for line in lines:
    num_str = line.rsplit()
    if not num_str :
        continue
    num_int = list(map(int, num_str))
    num_ls.append(num_int)


fw = open('culc_num.txt', 'w')

for num in num_ls :
    fw.write(f'{num[0]}+{num[1]}={num[0]+num[1]}\n')

fr.close()
fw.close()
