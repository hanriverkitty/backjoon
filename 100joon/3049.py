##대각선으로 생기는 교점의 최고수 == nC4
n = int(input())
sum=1
for i in range(n-3,n+1):
    sum*=i
    
print(sum//24)