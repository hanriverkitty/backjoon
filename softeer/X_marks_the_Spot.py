import sys
input = sys.stdin.readline
n = int(input())
arr1=[]
arr2=[]
for i in range(n):
    s1,s2 = input().split()
    arr1.append(s1)
    arr2.append(s2)

for i in range(n):
    a=arr1[i].find("x")
    b=arr1[i].find("X")
    
    if a!=-1:
        if(arr1[i][a].isdigit()):
            print(arr2[i][a],end="")
            
        else:
            print(arr2[i][a].upper(),end="")
    if b!=-1:
        if(arr1[i][b].isdigit()):
            print(arr2[i][b],end="")
        else:
            print(arr2[i][b].upper(),end="")
    