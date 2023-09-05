import sys
n = int(sys.stdin.readline().rstrip())
num_list=[]
for i in range(n):
    command=sys.stdin.readline().rstrip()
    if command=='pop':
        try:
            print(num_list[-1])
            num_list.pop(-1)
        except IndexError:
            print(-1)
    elif command=='size':
        print(len(num_list))
    elif command=='empty':
        if len(num_list)==0:
            print(1)
        else:
            print(0)
    elif command=='top':
        try:
            print(num_list[-1])
        except IndexError:
            print(-1)
    else:
        str,number = command.split()
        num_list.append(int(number))