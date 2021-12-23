# 함수 : 함수이름( )
# > input, print, len, del ...
# 메소드 : 객체이름.메소드이름( )

# .count( )
a = [1, 2, 3, 4, 1]
print(a.count(1)) # 요소의 개수 세기

# append( ), insert( )
a.append(1) # 마지막 자리에 1추가
a.insert(0, 1) # 0 번째 자리에 숫자 1 추가 (위치, 값)
print(a)
print(a.count(1))

# ---

scores = []

for i in range(10):
    scores.append(int(input('학생 점수 입력 : ')))

print(scores)