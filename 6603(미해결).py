import sys

input = sys.stdin.readline


def dfs(stack_arr, ind):
    if len(stack_arr) == 6:
        print(*stack_arr)
        return
    for i in range(ind, a):
        stack_arr.append(arr[i])
        dfs(stack_arr, ind + 1)
        stack_arr.pop()


while True:
    arr = list(map(int, input().split()))
    a = arr.pop(0)
    if a == 0:
        break
    dfs([], 0)
    print()
