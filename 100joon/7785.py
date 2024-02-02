import sys

input = sys.stdin.readline
####추가삭제 작업은 해쉬방식인 딕셔너리 형태가 빠르다
arr = {}
n = int(input())
for i in range(n):
    a, b = input().split()
    if b == "enter":
        arr[a] = "enter"
    elif b == "leave":
        del arr[a]

for i in sorted(arr.keys(), reverse=True):
    print(i)
