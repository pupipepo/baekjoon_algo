n = int(input())
import string
upper_list = string.ascii_uppercase
command = input()
num_list=[]
ans_list=[]
for i in range(n):
    num_list.append(int(input()))
for i in range(len(command)):
    if command[i]=='*':
        num_1 = ans_list.pop()
        num_2 = ans_list.pop()
        ans_list.append(num_1*num_2)
    elif command[i]=='+':
        num_1 = ans_list.pop()
        num_2 = ans_list.pop()
        ans_list.append(num_1+num_2)
    elif command[i]=='-':
        num_1 = ans_list.pop()
        num_2 = ans_list.pop()
        ans_list.append(num_2-num_1)
    elif command[i]=='/':
        num_1 = ans_list.pop()
        num_2 = ans_list.pop()
        ans_list.append(num_2/num_1)
        # print(ans_list)
    else:
        ans_list.append(num_list[upper_list.index(command[i])])
        # print(ans_list)
        
print(f'{ans_list[0]:.2f}')
    
    