def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
T = int(input())
ans_list=[]
for i in range(T):
  ans=0
  my_list = list(map(int, input().split()))
  nums = my_list[0]
  for j in range(1,nums):
    for k in range(j+1, nums+1):
      ans += gcd(my_list[j], my_list[k])
  ans_list.append(ans)
for i in range(len(ans_list)):
  print(ans_list[i])