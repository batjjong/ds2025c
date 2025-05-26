from collections import deque #bfs(append,popleft)

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]
#깊이우선방식
#Deep First Search
def dfs(g,i,visited):
    visited[i] = 1
    print(chr(ord('A')+i),end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g,j,visited)
#너비우선방식
#
def bfs(g,i,visited):
    while(deque.count() >= 1):
        deque.append(visited[i])


        deque.pop()
        print(chr(ord('A')+i),end=' ')

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]

dfs(graph,6,visited_dfs)
print()
bfs(graph,6,visited_bfs)
