import sys

input = sys.stdin.readline
n = int(input().rstrip())

for i in range(n):
    ans = []
    arr = list(input().rstrip())
    result = True
    for j in arr:
        if j == "(":
            ans.append(j)
        elif j == ")":
            try:
                ans.pop()
            except:
                print("NO")
                result = False
                break
    if len(ans) == 0 and result == True:
        print("YES")
    elif result == True:
        print("NO")
