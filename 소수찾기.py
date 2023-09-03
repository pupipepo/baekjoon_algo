nums = int(input())  # 숫자가 총 몇 개인지 알려줌
num_list = list(map(int, input().split(' ')))  # 공백 기준으로 나누어 int list로 받음
ans = 0


def is_prime(num):
  j = 2
  if num < 2:
    return False
  else:
    while j**2 <= num:
      if num % j == 0:
        return False
      else:
        j += 1
    return True


for i in range(nums):
  if is_prime(num_list[i]):
    ans += 1

print(ans)
