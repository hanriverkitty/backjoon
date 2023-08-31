import sys

input = sys.stdin.readline

arr = {}
n = int(input())
for i in range(n):
    name = input().rstrip()
    if name in arr:
        arr[name] += 1
    else:
        arr[name] = 1
dic = sorted(arr.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
