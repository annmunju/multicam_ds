students = {1:'최선', 2:'홍길동', 3:'강감찬'}

print(students)

prof = {}
prof[1] = '이순신'
prof[2] = '홍길동'

print(prof)

member = {'name' : '홍길동', 'phone' : '010-1234-1234'}
print(member)
print(member['name'])

print(member.keys())
print(member.values())
print(member.items())

print(member['name'])
print(member.get('name'))
key = 'id'
if member.get(key) is None:
    print(key + '값이 없습니다.')
# in이나 not in으로 포함 여부 판단할 수 있음.