from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a,b):
  
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                q.append((nx,ny))

bfs(0,0)
print(arr[n-1][m-1])
            
