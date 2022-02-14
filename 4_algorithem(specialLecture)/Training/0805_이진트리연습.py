class TreeNode():
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.data = None

memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root

    if current.data > node.data:
        if current.left == None:
            current.left = node
            break
        else :
            current = current.left
    else :
        if current.right == None:
            current.right = node
            break
        else :
            current = current.right    

    memory.append(node)

print('이진탐색완료!')


findData = '레드벨벳'

current = root
while True :
    if current.data == findData :
        print(findData, '찾음 ^^')
        break
    elif current.data > findData :
        if current.left == None :
            print(findData, ' 이 트리에 없음')
            break
        current =current.left
    else :
        if current.right == None :
            print(findData, ' 이 트리에 없음')
            break
        current =current.right