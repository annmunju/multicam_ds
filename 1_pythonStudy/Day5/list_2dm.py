# 2차원 리스트

data = [[1,2,3,4,5],\
        [6,7,8,9,10],\
        [11,12,13,14,15]]

print(data)

for r in range(len(data)):
    for c in range(len(data[0])):
        print(data[r][c], end='\t')