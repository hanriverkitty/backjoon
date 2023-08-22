import sys
input = sys.stdin.readline
n = int(input())
result=[]


def sosu(n):
    if n==1:
        return False
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
    return True
    
for i in range(n):
    num=int(input())
    a,b=num//2,num//2
    while a>0:
        if sosu(a) and sosu(b):
            result.append((a,b))
            break
        else:
            a-=1
            b+=1
            
for i,j in result:
    print(i,j)