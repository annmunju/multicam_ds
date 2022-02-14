partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

print(f"파티에 참석한 모든 사람\n{sorted(partyA | partyB)}")
print('-'*30)
print(f"2개의 파티에 모두 참석한 사람\n{sorted(partyA & partyB)}")
print('-'*30)
print(f"파티A에만 참석한 사람\n{sorted(partyA - partyB)}")
print('-'*30)
print(f"파티B에만 참석한 사람\n{sorted(partyB - partyA)}")