import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
circle = arr[0]

def sub(a):
    c=1
    count=1
    while(count<=a):
        if circle%count==0 and a%count==0:
            c=count
        count+=1
    return c

for i in range(1,n):
    if circle%arr[i]!=0:
        a = sub(arr[i])
        print(str(circle//a)+"/"+str(arr[i]//a))
    else:
        print(str(circle//arr[i])+"/"+str(1))
        
