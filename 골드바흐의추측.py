import sys

bool_list = []

for i in range(10000001):
  bool_list.append(0)
for i in range(2,1000001):
  if bool_list[i]==0:
    for j in range(i*2, 1000001, i):
      bool_list[j]=1

def Goldbach(num):
  for i in range(3, num//2, 2):
    if (bool_list[i]==0) and (bool_list[num-i]==0):
      return f'{num} = {i} + {num-i}'
  return f"Goldbach's conjecture is wrong"

while True:
  n=int(sys.stdin.readline().rstrip())
  if n==0:
    break
  print(Goldbach(n))