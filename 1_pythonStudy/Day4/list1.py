ls1 = []
print(ls1)
print(type(ls1))

ls2 = list()
print(ls2)
print(type(ls2))

ls3 = [1,2,3]
print(ls3)
print(type(ls3))

for i in ls3:
    print(i)

for i in range(0, len(ls3)):
    print(ls3[i], end = ' ')

print()
nums = [1,2,3]
a,b,c = nums # 길이가 같다면 각 자리에 대응됨
print(a, b, c)