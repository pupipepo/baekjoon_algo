N = int(input())
d = [-1]*(N+1)
d[0] = 0
a = [0] + list(map(int, input().split()))
for i in range(1,N+1):
  for j in range(1,i+1):
    if d[i] == -1 or d[i] > d[i-j] + a[j]:
      d[i] = d[i-j] + a[j]
print(d[N])