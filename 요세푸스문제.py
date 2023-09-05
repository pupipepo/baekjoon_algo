import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
first_list = deque(list(range(1,N+1)))
ans_str = '<'
for i in range(N-1):
    for j in range(K-1):
        first_list.append(first_list.popleft())
    ans_str += f'{first_list.popleft()}, '
ans_str += f'{first_list.popleft()}>'
print(ans_str)