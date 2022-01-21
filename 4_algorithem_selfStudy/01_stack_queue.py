stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.append(1)
stack.append(4)
print(stack[::-1])

# 데큐 라이브러리 사용 : 리스트로 구현하면 시간 복잡도가 큼

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
print(queue)
queue.reverse()
print(queue)