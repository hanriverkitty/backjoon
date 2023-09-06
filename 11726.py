import sys

input = sys.stdin.readline
a = int(input().strip())
arr = [0 for i in range(a + 2)]
arr[1] = 1
arr[2] = 2
for i in range(3, a + 1):
    arr[i] = arr[i - 2] + arr[i - 1]
print(arr[a] % 10007)
