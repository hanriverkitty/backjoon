import sys

a = sys.stdin.readline()
n = int(a)
arr = []
arr1 = []
arr2 = []
cnt = 0
result_cnt = 0
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append(a)
    arr1.append(b)
    arr2.append(c)
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if j == k or i == k:
                continue
            num = 100 * i + 10 * j + k
            num = str(num)
            st_cnt = 0
            b_cnt = 0
            cnt = 0
            for l in range(n):
                st_cnt, b_cnt = 0, 0
                for m in range(3):
                    if num[m] == str(arr[l])[m]:
                        st_cnt += 1
                    elif num[m] in str(arr[l]):
                        b_cnt += 1
                if arr1[l] == st_cnt and arr2[l] == b_cnt:
                    cnt += 1

            if cnt == n:
                result_cnt += 1

print(result_cnt)
