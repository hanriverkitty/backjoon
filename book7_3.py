import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr1 = [ i for i in range(max(arr)+1)]
a=0
def binary_search(arr,arr1,start,end,m):
    if start>end:
        return None
    mid = (start+end)//2
    sum = 0
    for i in arr:
        if(i>=arr1[mid]):
            sum+=i-arr1[mid]
   
    if sum==m:
        global a
        a = arr1[mid]
        return a
    elif sum>m:
        return binary_search(arr,arr1,mid+1,end,m)
    else:
        return binary_search(arr,arr1,start,mid-1,m)
        
    
    
    
print(binary_search(arr,arr1,0,len(arr1)-1,m))
