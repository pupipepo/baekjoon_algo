n, m = input().split()
n = int(n); m = int(m)
num_of_2 = 0
num_of_5 = 0
i = 2
while i <= n:
  num_of_2 += n//i
  i *= 2
i = 2
while i <= n-m:
  num_of_2 -= (n-m)//i
  i *= 2
i = 2
while i <= m:
  num_of_2 -= m//i
  i *= 2
i = 5
while i <= n:
  num_of_5 += n//i
  i *= 5
i = 5
while i <= n-m:
  num_of_5 -= (n-m)//i
  i *= 5
i = 5
while i <= m:
  num_of_5 -= m//i
  i *= 5

print(min(num_of_2, num_of_5))