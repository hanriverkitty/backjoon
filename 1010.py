import sys
n = int(input())
arr=[[0 for i in range(31)]for j in range(31)]
pro=[]

for i in range(1,31):
    for j in range(1,31):
        if i==1:
            arr[i][j]=j
            continue
        if i==j:
            arr[i][j]=1
            continue
        if i>j:
            continue
        else:
            arr[i][j] = arr[i][j-1]+arr[i-1][j-1]
        
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    pro.append([x,y])

for i in pro:
    print(arr[i[0]][i[1]])
    
    
    
