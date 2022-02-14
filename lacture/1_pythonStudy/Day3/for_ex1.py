num = 0
for i in range(1,11):
    num += i
print(num)

odd_num = 0
even_num = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_num += i
    else :
        odd_num += i

print(odd_num, even_num)

sumX = 0

for i in range(3,101,3):
    sumX += i
    print(i)

print(sumX)