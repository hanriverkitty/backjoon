from collections import deque
import sys

input = sys.stdin.readline
arr = []
n = int(input())
queue = deque()
while n > 0:
    a = input().rstrip()
    n = n - 1
    if "push_front" in a:
        a, b = a.split()
        queue.appendleft(b)
    elif "push_back" in a:
        a, b = a.split()
        queue.append(b)
    elif a == "pop_front":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif a == "pop_back":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif a == "size":
        print(len(queue))
    elif a == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif a == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
