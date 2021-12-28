A = {1, 2, 3}
B = {3, 4, 5}

# 교집합
print(A & B)
print(A.intersection(B))

# 합집합
print(A | B)
print(A.union(B))

# 차집합
print(B - A)
print(B.difference(A))
print(A - B)
print(A.difference(B))