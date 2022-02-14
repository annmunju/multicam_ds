## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre

    node = Node()
    node.data = insertData

    # 첫 노드, 앞 삽입
    if findData == head.data:
        node.link = head
        head = node
        return

    # 두번째 노드 이후, 앞 삽입
    current = head
    while current != None:
        pre = current
        current = current.link
        if current.data == findData:
            node.link = current
            pre.link = node
            return
    # current == None : 못찾았고, 마지막에 삽입
    current.link = node
    return

def deleteNode(deleteData) : 
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data :
        current = head
        head = head.link
        del(current)
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
        return Node()

## 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

insertNode('문주', '문별')
printNodes(head)

fNode = findNode('다현')
print(fNode.data)