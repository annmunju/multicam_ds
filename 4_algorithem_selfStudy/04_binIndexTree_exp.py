# 데이터 개수 n, 변경 횟수 m, 구간 합 계산 횟수 k
n, m, k = map(int,input().split())

# 1. 빈 배열 만들기
arr = [0] * (n+1) # 0을 포함하는 배열 저장소
tree = [0] * (n+1) # 0을 포함하는 트리 합산 저장소

# 2. 인덱스(i)를 기준으로 i & -i 가 본인이 나오기 전까지 누적합.
def prefix_sum(i): # fix 이전의 합산 저장. i가 가장 마지막 값일 때
    result = 0
    while i > 0 :
        result += tree[i]  
        i -= (i & -i) # 2의 ?제곱인 수의 경우 i -= (i & -i) 는 0이 됨.
    return result # 처음 인덱스(0)부터 해당 인덱스(i) 까지의 누적합 반환

# 3. 특정 값이 변경되는 경우, 변경된 값을 포함하는 모든 누적합을 변경해야 함
def update(i, dif): # i : 인덱스, dif : 현재 값과 바꿀 값의 차이
    while i <= n: # 위와 반대로 올라가면서 적용
        tree[i] += dif 
        i += (i & -i) # i가 n 이하의 2의 ?제곱인 수 까지 가야해..!

# 4. 구간 누적합 계산
def interval_sum(start, end): 
    return prefix_sum(end) - prefix_sum(start-1) # 끝 누적 - (시작+1) 누적

# ---트리완성---

for i in range(1, n+1):
    x = int(input())
    arr[i] = x # arr에 해당 배열 업데이트
    update(i, x) # 트리에 누적합 업데이트

for i in range(m+k):
    a, b, c = map(int, input().split())
    # 업데이트 연산
    if a == 1:
        update(b, c - arr[b]) # dif(바꾸고자 하는 값 - 원본 값 = c - arr[b])
        arr[b] = c # arr[b] 값을 c로 업데이트!
    # 구간 누적 합 print
    else :
        print(interval_sum(b, c))


    