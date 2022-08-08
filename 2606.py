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


dfs(1)
print(cnt)
