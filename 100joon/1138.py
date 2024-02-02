import sys

input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))
result = [0 for i in range(n)]

for i in range(n):
    temp = ll[i]
    cnt = 0
    for j in range(n):
        if result[j] == 0 and cnt == temp:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(" ".join(map(str, result)))
