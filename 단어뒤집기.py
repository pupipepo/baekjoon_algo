T = int(input())
for i in range(T):
  sen = input()
  sen = sen + ' '
  temp = []
  ans_list=[]
  for j in sen:
    if j == ' ':
      while len(temp)>0:
        ans_list.append(temp.pop())
      ans_list.append(' ')
    else:
      temp.append(j)
  print(''.join(ans_list))