import sys

input = sys.stdin.readline

arr = list(input().rstrip().split("-"))
cnt = 0
if len(arr) == 1:
    sum_arr = list(map(int, arr[0].split("+")))
    cnt = sum(sum_arr)
    print(cnt, end="")

else:
    cnt = 2 * sum(list(map(int, arr[0].split("+"))))
    for i in arr:
        if "+" in i:
            sum_arr = list(map(int, i.split("+")))
            cnt -= sum(sum_arr)

        else:
            cnt -= int(i)
    print(cnt, end="")
