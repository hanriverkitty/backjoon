import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
circle = arr[0]

#유클리드 호제법
def sub(a,b):
    while (b>0):
        a,b=b,a%b
    return a

for i in range(1,n):
    if circle%arr[i]!=0:
        a = sub(circle,arr[i])
        print(str(circle//a)+"/"+str(arr[i]//a))
    else:
        print(str(circle//arr[i])+"/"+str(1))
        
