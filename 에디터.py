import sys
left_stack = list(sys.stdin.readline().rstrip())
right_stack =[]
n_lines = int(sys.stdin.readline().rstrip())
for i in range(n_lines):
    command = sys.stdin.readline().rstrip()
    if command[0]=='P':
        command, letter = command.split(' ')
        left_stack.append(letter)
    elif command[0]=='L':
        if len(left_stack)!=0:
            right_stack.append(left_stack.pop())
    elif command[0]=='D':
        if len(right_stack)!=0:
            left_stack.append(right_stack.pop())
    elif command[0]=='B':
        if len(left_stack)!=0:
            left_stack.pop()
while len(left_stack)>0:
    right_stack.append(left_stack.pop())
while len(right_stack)>0:
    print(right_stack.pop(), end='')