from re import search

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')

def in_order(node):
    if node:
        post_order(node.left)
        print(node.data, end='->')
        post_order(node.right)


def pre_order(node):
    if node:
        print(node.data, end='->')
        post_order(node.left)
        post_order(node.right)


def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:  # 첫 번째 노드 처리
        return new_node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return root

def search(find_number):
    current = root
    while True:
        if find_number == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    # 1번째 원소 부터 마지막 원소까지
    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")

    post_order(root)  # 3-9-8-15-10
    print()
    in_order(root)
    print()
    pre_order(root)
    print()

    number = int(input("찾는 값 입력 : "))
    if search(number):
        print(f"{number}을(를) 찾았습니다")
    else:
        print(f"{number}이(가) 존재하지 않습니다")