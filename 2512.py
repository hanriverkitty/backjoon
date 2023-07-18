import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n=int(input())

arr = list(map(int,(input().split())))
arr.sort()
m = int(input())
if sum(arr)>m:
    budget= arr[0]
    start,end=0,arr[-1]
    while(start<=end):
        #이분탐색
        mid = (start+end)//2
        cost = 0
        for i in arr:
            if i>mid:
                cost+=mid
            else:
                cost+=i
        
        if cost>m:
            end = mid-1
        else:
            start = mid+1
        
    print(end)
        
        
        ###시간초과###
        ###그리디###
        # k=-1
        # all=0
        # for i in range(len(arr)):
        #     k+=1
        #     if arr[i]<=budget:
        #         all+=arr[i]

        #     else:
        #         break
        
        
        # all=all+(budget*(len(arr)-(k)))

        # if all>=m:
        #     print(budget-1)
        #     break
        # budget+=1    
        
        # all = 0
        # for i in arr:
        #     if budget>i:
        #        all+=i
        #     else:
        #         all+=budget 
        # if all>=m:
        #     print(budget-1)
        #     break
        # else:
        #     budget+=1
    
else:
    budget = max(arr)
    print(budget)