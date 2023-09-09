import string
s=string.ascii_lowercase
ans=[]
S=input()
for i in range(len(s)):
    ans.append(S.count(s[i]))
print(*ans)