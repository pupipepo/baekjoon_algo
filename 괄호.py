T=int(input())
def is_vps(my_str):
    if len(my_str)%2 != 0:
        print('NO')
    else:
        for i in range(25):
            my_str=my_str.replace('()','')
        if len(my_str)==0:
            print('YES')
        else:
            print('NO')

for j in range(T):
    is_vps(input())