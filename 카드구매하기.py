N = int(input())
d = [0]*(N+1)
a = [0] + list(map(int, input().split()))
for i in range(1,N+1):
  for j in range(1,i+1):
    d[i] = max(d[i], d[i-j]+a[j])
print(d[N])