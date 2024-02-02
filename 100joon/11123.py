import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result_arr=[]

def dfs(m,n):
    if m<0 or n>=y or n<0 or m>=x:
        return False
    if arr[m][n]=="#":
        arr[m][n]="."
        for i in range(4):
            dfs(m+dx[i],n+dy[i])
        return True
    return False

T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    arr = [[] for _ in range(x)]
    
    for j in range(x):
        arr[j]=list(input().rstrip())    

    result=0
    for k in range(y):
        for l in range(x):
            if dfs(l,k)==True:
                result+=1
    result_arr.append(result)
for i in result_arr:
    print(i)