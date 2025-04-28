from queue import Queue

q =Queue()
q.put("Database")
q.put("Data Structure")

print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
#print(q.size, q.front.data, q.rear.data) 프론트과 리어 값은 None
#print(q.dequeue()) 인덱스 에러가 남