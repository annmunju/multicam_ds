## 함수
def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (rear == front) :
		return True
	else :
		return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty() :
        return '큐 텅!'
    front += 1
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('선미')
enQueue('아이유')

enQueue('?')
print('출구 <--', queue, '<-- 입구')

print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print('출구 <--', queue, '<-- 입구')




