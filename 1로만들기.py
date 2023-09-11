num = int(input())
ans_list = [0]*(num+1)
for i in range(2,num+1):
  ans_list[i] = ans_list[i-1]+1
  if i%2 == 0 and ans_list[i//2]+1 < ans_list[i]:
    ans_list[i] = ans_list[i//2]+1
  if i%3 == 0 and ans_list[i//3]+1 < ans_list[i]:
    ans_list[i] = ans_list[i//3]+1
print(ans_list[num])