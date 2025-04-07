class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node  # top update

    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None #연결 끊음
        return popped_node.data


s1 = Stack()
print(s1.pop())#21번 라인 실행 스택이 빈 상태
s1.push("Data structure")
s1.push("Database")
print(s1.pop())
print(s1.pop())
print(s1.pop())#스택이 빈 상태