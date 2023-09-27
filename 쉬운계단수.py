import sys
input = sys.stdin.readline
limit = 100
mod = 1000000000
d = [[0]*10 for _ in range(limit+1)]
d[1] = [1]*10
d[1][0] = 0
for i in range(2, limit+1):
  for j in range(10):
    if j-1 >=0:
      d[i][j] += d[i-1][j-1]
    if j+1 <=9:
      d[i][j] += d[i-1][j+1]
    d[i][j] %= mod
n = int(input())
print(sum(d[n])%mod)