import sys
input = sys.stdin.readline
n = int(input())

def go(num,k):
    cnt = 0
    while num:
        cnt+=num//k
        num//=k
    return cnt

print(min(go(n,2),go(n,5)))