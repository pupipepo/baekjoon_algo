n, X = input().split()
n = int(n) # 동생의 명수
X = int(X) # 나의 위치
brother_list = list(map(int, input().split()))

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)

if n==1:
  ans = brother_list[0]-X
else:
  ans = gcd(brother_list[0]-X, brother_list[1]-X)
for i in range(2, len(brother_list)):
  ans = gcd(ans, brother_list[i]-X)
if ans <0:
  print(-ans)
else:
  print(ans)