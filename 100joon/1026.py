N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = B
result = 0
A.sort()
for i in range(0, len(c)):
    max_n = max(c)
    min_n = min(A)
    A.remove(int(min_n))
    c.remove(int(max_n))
    result += max_n*min_n


print(result)
