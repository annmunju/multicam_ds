# 파일 내에서 검색
# seek(상대(열) 위치, 0(파일 시작 위치) | 1(현재위치) | 2(파일 끝 위치)
# seek(0, 0) : 시작 위치로부터 0열의 위치
# seek(10, 0) : 시작 위치로부터 오른쪽 10열의 위치

f = open('file2.txt', 'r')
f.seek(12,0)
lines = f.readline()
print(lines)
f.close()

# \r : carriage return (첫열로 이동)
# \n : line feed (다음줄로 이동)
# 텍스트 파일에서 엔터키를 누르면 '\r\n'이 자동으로 입력되는 것과 같음
