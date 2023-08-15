import sys
sys.setrecursionlimit(10**7)

a,b = map(int,input().split())

if a-b<b:
    b=a-b

#팩토리얼에 들어가는 인수의 개수는 n!이라 했을때, n을 i의 지수승들로 나눈 몫들의 합
# 10! 에 들어가는 2의 인수의 개수는 (10//2 = 5) + (10//4 = 2) + (10//8 = 1)
def go(num,k):
    count=0
    div=k
    while div<=num:
        count+=num//div
        div*=k
    return count

cnt_2 = go(a,2)-go(b,2)-go(a-b,2)
cnt_5 = go(a,5)-go(b,5)-go(a-b,5)
print(min(cnt_2,cnt_5))