import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]

result = []
count = 0
while arr:
    count += k - 1
    if count >= len(arr):
        count %= len(arr)
    result.append(arr.pop(count))

print("<", end="")
for i in range(len(result) - 1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">")
