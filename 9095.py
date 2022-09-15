n = int(input())

arr=[0 for _ in range(12)]

arr[0]=0
arr[1]=1
arr[2]=2
arr[3]=4
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(4,12):
    for j in range(1,4): 
        arr[i] += arr[i-j]
        

for i in a:
    print(arr[i])