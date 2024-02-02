from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]
def bfs(arr2):
    global cnt
    q=deque(arr2)
    print(q)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx<0 or nx>=m or ny<0 or ny>=n):
                continue
            if(arr[nx][ny]==-1):
                continue
            if(arr[nx][ny]==0):
                #탐색마다 값을 다르게 저장하여 중복되는상황 방지
                arr[nx][ny]=arr[x][y]+1
                q.append((nx,ny))
        for i in arr:
            print(i)
        print()
arr2=[]
for i in range(m):
        for j in range(n):
            if(arr[i][j]==1):
                arr2.append((i,j))
print(arr2)
def check():
    #탐색전에 0이 없으면 return 0 
    a=0
    for i in range(m):
        for j in range(n):
            if(arr[i][j]!=0):
                a+=1       
    if n*m==a:
        return 0 
    
    
    #탐색                          
    
    bfs(arr2)
               
    
    #탐색후 0이 남아있으면 return -1
    for i in range(m):
        for j in range(n):
            if(arr[i][j]==0):
                return -1
            
    #탐색후 서로 다른 값이 몇개있는지 비교하기 위해 요소들을 전부 다른 리스트에 넣어준다
    arr1=[]
    for i in range(m):
        for j in range(n):
            if (arr[i][j] != 1 and arr[i][j] != -1):
                arr1.append(arr[i][j])
    #처음에 1일 경우를 빼고 카운트
    set_arr= list(set(arr1))
    print(set_arr)
    return len(set_arr)
    
    
            
print(check())
            