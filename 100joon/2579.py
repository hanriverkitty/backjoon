import sys
input = sys.stdin.readline
n = int(input())
arr=[0]

for i in range(n):
    arr.append(int(input()))

result=[0]*(n+1)
result[1]=arr[1]
if n>=2:
    result[2]=arr[2]+arr[1]
    for i in range(3,n+1):
        result[i]=max(result[i-3]+arr[i-1]+arr[i],result[i-2]+arr[i])
    
print(result[-1])
