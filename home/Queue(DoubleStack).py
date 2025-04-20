from os import remove

class Queue:
    def __init__(self):
        self.s1 = [] #스택 1
        self.s2 = [] #스택 2
    def enqueue(self,item):
        print(f"enqueued item: {item}")
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
            print(f"s1 -> s2: {item}, 현재 s1: {self.s1}, s2: {self.s2}")
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
            print(f"s2 -> s1: {item}, 현재 s1: {self.s1}, s2: {self.s2}")
    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("cannot pop from empty queue")
        removed = self.s1.pop()
        print(f"dequeued item: {removed}")
        return removed
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()

