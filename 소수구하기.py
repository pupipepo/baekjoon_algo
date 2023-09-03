n, m = input().split(' ')
n= int(n)
m= int(m)
# num_list = list(range(2,m+1))
bool_list=[]
for i in range(m+1):
  bool_list.append(0)
for i in range(2,m+1):
  if bool_list[i]==0:
    for j in range(i*2, m+1, i):
      bool_list[j]=1
for i in range(n,m+1):
  if i>1:
    if bool_list[i]==0:
      print(i)