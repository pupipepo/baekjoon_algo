def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
T = int(input())
ans_list=[]
for i in range(T):
    n, m = input().split()
    n = int(n); m = int(m)
    ans_list.append(n*m//gcd(n,m))
for i in range(T):
    print(ans_list[i])