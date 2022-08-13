import sys
sys.setrecursionlimit(10**7)

n = int(input())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
print(arr)
cnt = 2 
result=0
def dfs(x,y,cnt):
    if(x<0 or x>=n or y<0 or y>=n):
        return False
    if(arr[x][y]==1):
        arr[x][y]=cnt
        dfs(x-1,y,cnt)
        dfs(x+1,y,cnt)
        dfs(x,y+1,cnt)
        dfs(x,y-1,cnt)
        return True
    return False
    
for i in range(n):
    for j in range(n):
        if dfs(i,j,cnt) == True:
            result+=1
            cnt+=1
print(result)
a_cnt = []
count=0
for i in range(cnt-1,1,-1):
    for j in range(n):
        count+=arr[j].count(i)
    a_cnt.append(count)
    count=0  
a_cnt.sort()
for i in a_cnt:
    print(i)
