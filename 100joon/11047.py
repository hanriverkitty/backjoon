a, b = map(int, input().split())
k = []
l = []
cnt = 0
# take N types
for i in range(a):
    m = int(input())
    k.append(m)
k.reverse()

# make list can divide b
for i in range(len(k)):
    if(b//k[i] != 0):
        l.append(k[i])

# search which can divide and count
for i in range(len(l)):
    if(b//l[i] != 0):
        cnt += b//l[i]
        b = b-(b//l[i]*l[i])
        if(b == 0):
            break
print(cnt)
