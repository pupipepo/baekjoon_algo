bool_list = []
for i in range(10000001):
  bool_list.append(0)
for i in range(2,1000001):
  if bool_list[i]==0:
    for j in range(i*2, 1000001, i):
      bool_list[j]=1
while True:
  n = int(input())
  if n==0:
    break
  small_num=3
  while small_num <= n//2:
    if bool_list[small_num]==0:
      if bool_list[n-small_num]==0:
        print(f'{n} = {small_num} + {n-small_num}')
        break
      else:
        small_num+=2
    else:
      small_num+=2
  print("Goldbach's conjecture is wrong.")