import sys
n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ans_list = []
freq_list = []
for i in range(1000001):
    freq_list.append(0)
for i in range(n):
    freq_list[num_list[i]] += 1
    ans_list.append(-1)
my_stack=[0]
ans_str=''
for i in range(1,n):
    while freq_list[num_list[i]] > freq_list[num_list[my_stack[-1]]]:
        ans_list[my_stack[-1]] = num_list[i]
        my_stack.pop()
        if len(my_stack)==0:
            my_stack.append(i)
    my_stack.append(i)
    
print(*ans_list)