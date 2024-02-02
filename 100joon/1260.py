from collections import deque

n, m, v = map(int, input().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited = [0]*(n+1)


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


def bfs(v):
    # deque는 시작점이므로 안에서 한번만 실행
    queue1 = deque([v])
    visited[v] = 0
    while queue1:
        c = queue1.popleft()
        print(c, end=" ")
        for i in graph[c]:
            if visited[i] == 1:
                queue1.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
