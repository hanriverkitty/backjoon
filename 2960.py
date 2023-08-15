n,k = map(int,input().split())
arr = [i for i in range(2,n+1)]
arr2=arr[:]
arr1=[]
for i in arr:
    j=1
    a=1
    while a<=n:
        if (i*j in arr) and (i*j not in arr1):
            arr1.append(i*j)
        a=i*j   
        j+=1
        if len(arr1)==k:
            break
    if len(arr1)==k:
            break       
     
print(arr1[k-1])


###########
"""
n, k = map(int, input().split())

data = [True for i in range(n + 1)]
count = 0

for i in range(2, len(data) + 1) :
  for j in range(i, n+1, i) :
    if data[j] :
      data[j] = False
      count += 1
      if count == k :
        print(j)
        break
"""
##############