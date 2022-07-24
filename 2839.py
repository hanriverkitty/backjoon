a = int(input())
k = []
if(a//5 != 0):
    if(a % 5 == 0):
        print(a//5)
    else:
        for i in range(0, a//5+1):
            if((a-i*5) % 3 == 0):
                c = (a-i*5)//3
                k.append(i+c)
        if(k):
            print(min(k))
        else:
            print(-1)
elif(a//3 != 0):
    if(a % 3 == 0):
        print(a//3)
    else:
        print(-1)
