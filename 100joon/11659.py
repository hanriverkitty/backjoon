import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
result_arr1=[]
max_num=0
for i in range(m):
    a,b = map(int,input().split())
    result_arr1.append((a,b))
    max_num=max(a,b,max_num)
result=[0]

temp=0
for i in range(max_num):
    temp+=arr[i]
    result.append(temp)

for i,j in result_arr1:
    print(result[j]-result[i-1])
        
# def sum1(a,b):
#     result=0
#     for i in range(a-1,b):
#         result+=arr[i]
#     return result

# for i in range(m):
#     a,b = map(int,input().split())
#     result_arr.append(sum1(a,b))

# for i in result_arr:
#     print(i)