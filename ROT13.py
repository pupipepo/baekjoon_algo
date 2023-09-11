from string import ascii_lowercase
from string import ascii_uppercase

sen = input()
ans_list=[]
for i in sen:
  if i in ascii_lowercase:
    ans_list.append(ascii_lowercase[(ascii_lowercase.find(i)+13)%26])
  elif i in ascii_uppercase:
    ans_list.append(ascii_uppercase[(ascii_uppercase.find(i)+13)%26])
  else:
    ans_list.append(i)
print(''.join(ans_list))