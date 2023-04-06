import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr=[0 for _ in range(k+1)]
won=[]
for i in range(n):
    a=(int(input()))
    won.append(a)
won.sort()
arr[0]=1
for i in won:
    for j in range(1,k+1):
    
        if j-i>=0:
            arr[j]=arr[j]+arr[j-i]
print(arr[-1])