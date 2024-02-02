import sys
t = int(input())
arr0=[0 for _ in range(41)]
arr1=[0 for _ in range(41)]
a=[]
arr0[0]=1
arr0[1]=0
arr0[2]=1
arr1[0]=0
arr1[1]=1
arr1[2]=1
for i in range(t):
    a.append(int(input()))

for j in range(3,41):
    arr0[j] = arr0[j-1]+arr0[j-2]
    arr1[j] = arr1[j-1]+arr1[j-2]
        

for i in range(t):
    print(arr0[a[i]],arr1[a[i]])
  
    