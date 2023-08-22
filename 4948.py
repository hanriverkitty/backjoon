import sys
input = sys.stdin.readline

num=[]
while True:
    a=int(input())
    if a==0:
        break
    else:
        num.append(a)
        
arr=[0 for i in range(2*max(num)+1)]    
arr[2]=1
   
for i in range(3,len(arr)):
    aa=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            aa=False
            break
    if aa==True:
        arr[i]=arr[i-1]+1
    else:
        arr[i]=arr[i-1]
       
        
for i in num:
    print(arr[i*2]-arr[i])
    
    

    