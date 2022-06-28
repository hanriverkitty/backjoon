a = int(input())
l = []
for i in range(a):
    b, c = map(int, input().split())
    l.append(b+c)
for i in l:
    print(i)
