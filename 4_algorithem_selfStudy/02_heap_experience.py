import heapq

orderList = list(map(int, input("빠르게 순서 정리할 리스트 입력(띄어쓰기): ").split()))
h = []
result = []

for i in orderList:
    heapq.heappush(h, i)

for _ in range(len(orderList)):
    result.append(heapq.heappop(h))

print(result)
