import sys
sys.setrecursionlimit(10**7)
t = int(input())


def take_n():
    m, n, k = map(int, input().split())
    arr = [[0 for i in range(n)]for j in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j, m, n, arr) == True:
                result += 1
    return result


def dfs(x, y, m, n, arr):
    if(x < 0 or x >= m or y < 0 or y >= n):
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x-1, y, m, n, arr)
        dfs(x+1, y, m, n, arr)
        dfs(x, y-1, m, n, arr)
        dfs(x, y+1, m, n, arr)
        return True
    return False


q = []
for l in range(t):
    q.append(take_n())
for i in range(len(q)):
    print(q[i])
