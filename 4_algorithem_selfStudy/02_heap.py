
import heapq

def heapsort(iterable): 
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return h

arr = list(map(int, input('힙에 삽입할 숫자 띄어쓰기로 입력 : ').split()))

res = heapsort(arr)

# for i in range(len(arr)):
#     print(res[i])
print(res)
