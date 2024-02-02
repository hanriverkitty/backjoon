import sys
sys.setrecursionlimit(10**7)

n = int(input())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
cnt = 2 
result=0
#dfs 탐색
def dfs(x,y,cnt):
    if(x<0 or x>=n or y<0 or y>=n):
        return False
    if(arr[x][y]==1):
        #cnt로 각각 다른 단지 부여
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
            #깊이 탐색을 다한 후 결과값 증가 단지값 증가
            result+=1
            cnt+=1
print(result)
print(arr)
a_cnt = []
count=0
#각각의 단지가 몇개 인지 탐색
for i in range(cnt-1,1,-1):
    for j in range(n):
        count+=arr[j].count(i)
    a_cnt.append(count)
    #0으로 초기화후 다른단지 재탐색
    count=0  
a_cnt.sort()
for i in a_cnt:
    print(i)
