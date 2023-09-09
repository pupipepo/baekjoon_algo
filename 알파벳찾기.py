from string import ascii_lowercase

alphab = list(ascii_lowercase)
A = input()
ans=[]
for i in range(len(alphab)):
    ans.append(A.find(alphab[i]))
print(*ans)