a = int(input())
k = list(map(int, input().split()))
result = 0
# for i in range(len(k)-1):
#     for j in range(len(k)-1):
#         if(k[j] > k[j+1]):
#             k[j], k[j+1] = k[j+1], k[j]
k.sort()
for i in range(len(k)):
    for j in range(i+1):
        result += k[j]

print(result)
