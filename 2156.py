n = int(input())
arr=[0]
for i in range(n):
    arr.append(int(input()))
ans=[0 for _ in range(n+1)]
ans[1]=arr[1]
if n>=2:
    ans[2]=arr[1]+arr[2]
if n>=3:
    ans[3]=max(arr[1]+arr[2],arr[2]+arr[3],arr[1]+arr[3])    
for i in range(4,n+1):
    ans[i] = max(ans[i-3]+arr[i]+arr[i-1],ans[i-2]+arr[i],ans[i-1])
    
print(ans[n])