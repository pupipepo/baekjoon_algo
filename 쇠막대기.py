import sys
pipe = sys.stdin.readline().rstrip()
my_stack=[]
ans=0
for i in range(len(pipe)):
    if pipe[i]=='(':
        my_stack.append(i)
    elif my_stack[-1]+1==i:
        my_stack.pop()
        ans += len(my_stack)
    else:
        my_stack.pop()
        ans += 1 
print(ans)