a = int(input())
k = []
if(a//5 != 0):
    # completely divided by 5
    if(a % 5 == 0):
        print(a//5)

    else:
        # search situation which can be made by 5 and 3, then add to list
        for i in range(0, a//5+1):
            if((a-i*5) % 3 == 0):
                c = (a-i*5)//3
                k.append(i+c)
        # print minimum count
        if(k):
            print(min(k))

        # can divided by 5, but rest can't divided by 3
        else:
            print(-1)

 # can divide 3
elif(a//3 != 0):
    # only divided by 3
    if(a % 3 == 0):
        print(a//3)

    # 3 and 5 can't divide
    else:
        print(-1)


"""
a = int(input())
cnt = 0

while a >= 0:
  if a % 5 == 0:
    cnt += int(a // 5)
    print(cnt)
    break
  
  a -= 3
  cnt += 1
  
else:
  print(-1)
"""
