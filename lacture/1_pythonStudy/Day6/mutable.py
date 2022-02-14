# 튜플 변경 불가
x = (1,2)
y = x
y = y + (3,)
print(x)
print(y)

# 리스트 변경 (원본 변경)
x = [1,2]
y = x
y.append(3)
print(x)
print(y)

# 딕셔너리 변경 (원본 변경)
x = {1:2}
y = x
y[2] = 3
print(x)
print(y)