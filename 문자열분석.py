from string import ascii_lowercase
from string import ascii_uppercase

lower = ascii_lowercase
upper = ascii_uppercase
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
  
  try:
    sen = input()
    lower_num = 0
    upper_num = 0
    number_num = 0
    blank_num = 0
    for i in sen:
      if i in lower:
        lower_num += 1
      elif i in upper:
        upper_num += 1
      elif i in num:
        number_num += 1
      else:
        blank_num += 1
    print(f'{lower_num} {upper_num} {number_num} {blank_num}')
  except EOFError:
    break