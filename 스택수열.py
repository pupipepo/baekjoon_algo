n_lines = int(input())
num_top_stack = 0
num_oreum = 0
my_list =[]
print_list=[]
is_fault = False
for i in range(n_lines):
    num_wanted = int(input())
    while num_wanted > num_top_stack:
        num_oreum += 1
        my_list.append(num_oreum)
        num_top_stack = my_list[-1]
        print_list.append('+')
        # print(num_oreum)
    if num_wanted == num_top_stack:
        my_list.pop()
        if len(my_list)==0:
            num_top_stack = 0
            print_list.append('-')
        else:
            num_top_stack = my_list[-1]
            print_list.append('-')
    else:
        is_fault = True

if is_fault:
    print('NO')
else:
    for j in range(len(print_list)):
        print(print_list[j])
    