'''

x = [1, 8, -1]

# append(값) : 리스트의 마지막에 값을 삽입
# insert(위치, 값) : 리스트의 원하는 위치에 값을 삽입
x.insert(-1, 20)
print(x)

# 리스트의 요소 제거

# remove(값) : 리스트의 원하는 값에 해당하는 가장 첫번째 내용을 제거 (여러개 제거시 반복문 이용)
# pop() : 마지막의 요소 값을 제거

h = x.pop()
print(h, x)

# extend() : 리스트 확장
y = [2,3,4]

x.extend(y)
print(x)

# sort(), reverse() : 리스트 정렬, 리스트 반대정렬. 리스트가 바뀜
# sorted(리스트) : 리스트 정렬. 원본 리스트는 변경되지 않음.
y.reverse()
print(y)
x.sort()
print(x)
print(sorted(x, reverse=True))
print(x)

'''

# .sort(key=)
chr = ['b', 'A', 'e', 'C']
print(chr)
chr.sort(key=str.lower) # 대소문자 구별 없이 정렬
print(chr)

for idx, value in enumerate(chr):
    print(idx, value)

print(max(chr))
print(min(chr))