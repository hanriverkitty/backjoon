import sys
input = sys.stdin.readline

n,k = map(int,input().split())

if k==0:
    print(1)
elif k==n:
    print(1)
else:
    arr=[]
    for i in range(n+1) :
        arr.append([1]*(i+1))
    for i in range(2,n+1):
        arr[i][0]=1
        for j in range(1,i):
            arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])%10007

    print(arr[n][k])