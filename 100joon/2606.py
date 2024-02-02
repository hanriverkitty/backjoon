from collections import deque
N = int(input())
m = int(input())
arr = [[] for j in range(N+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
visited = [0]*(N+1)


def dfs(start):
    global cnt
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

def bfs(start):
    global cnt
    visited[start] = 1
    q=deque([start])
    while q:
        a=q.popleft()
        for i in arr[a]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
        cnt+=1        
        
bfs(1)

print(sum(visited)-1)

