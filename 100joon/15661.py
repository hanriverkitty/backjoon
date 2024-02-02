#시간 복잡도 에러로 인해 zip을 활용해 sum을 미리 해주어야한다


import sys
input = sys.stdin.readline
ans = sys.maxsize
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))
     
team = [0 for _ in range(n)]

def calculate():
    global ans
    start, link = 0,0
    for i in range(n-1):
        for j in range(i+1,n):
            if team[i] and team[j]:
                start += arr[i][j] + arr[j][i]
            elif not team[i] and not team[j]:
                link += arr[i][j] + arr[j][i]
    ans = min(ans,abs(start-link))
    return

def divide(a):
    if a==n:
        calculate()
        return
    
    team[a]=1
    divide(a+1)
    team[a]=0
    divide(a+1)
    
divide(0)
print(ans)