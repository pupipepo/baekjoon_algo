from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
ans_deque = deque()
for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0]=='push_front':
        ans_deque.appendleft(command[1])
    elif command[0]=='push_back':
        ans_deque.append(command[1])
    elif command[0]=='size':
        print(len(ans_deque))
    elif ans_deque:
        if command[0]=='pop_front':
            print(ans_deque.popleft())
        elif command[0]=='pop_back':
            print(ans_deque.pop())
        elif command[0]=='empty':
            print(0)
        elif command[0]=='front':
            print(ans_deque[0])
        elif command[0]=='back':
            print(ans_deque[-1])
    else:
        if command[0]=='empty':
            print(1)
        else:
            print(-1)