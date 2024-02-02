import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
arr1=[0 for i in range(n)]
for i in range(n):
    arr1[i]=arr[i]*(n-i)
print(max(arr1))