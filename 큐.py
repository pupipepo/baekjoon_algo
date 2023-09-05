import sys
n_lines = int(sys.stdin.readline().rstrip())
ans_list=[]
for _ in range(n_lines):
    command = sys.stdin.readline().rstrip().split(' ')
    if command[0] == 'push':
        ans_list.append(command[1])
    elif command[0] == 'size':
        print(len(ans_list))
    elif ans_list:
        if command[0] == 'pop':
            print(ans_list.pop(0))
        elif command[0] == 'empty':
            print(0)
        elif command[0] == 'front':
            print(ans_list[0])
        elif command[0] == 'back':
            print(ans_list[-1])
    else:
        if command[0] == 'empty':
            print(1)
        else:
            print(-1)