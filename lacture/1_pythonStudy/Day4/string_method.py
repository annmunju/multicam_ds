# len()
# count()
# find()
# index()
# split()
# replace()
# join()
# upper() / lower() / capitalize()
# strip() / l~ r~

string = 'programming'
print(len(string))

print(string.count('r'))
print(string.count('m'))
print(string.count('ing'))

crawling = 'Data craling is fun'
print(crawling.find('is'))
print(crawling.find('is', 15)) #찾는 문자열 없는 경우 -1 반환

print(crawling.index('is')) #찾는 문자열 없는 경우 에러 발생