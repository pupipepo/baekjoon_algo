import sys
my_str = sys.stdin.readline().rstrip() #문제 문장 입력받기

def print_reverse(some_list): #stack 안에 있는 문자열 거꾸로 출력하기
    while some_list:
        print(some_list.pop(), end='')

ans_list = [] # 뒤집을 문자열 저장소
is_tag = False # tag flag
for i in range(len(my_str)): # 문자열 전체를 뒤지면서 돌아가는 for 구문
    if my_str[i]=='<': # tag 시작을 만나면
        print_reverse(ans_list) # 이전에 담아 두었던 것 모두 거꾸로 출력
        is_tag = True # tag flag on
        print(my_str[i], end='') # < 그대로 출력
    elif my_str[i]=='>': # tag 끝을 만나면
        is_tag = False # tag flag off
        print(my_str[i], end='') # > 그대로 출력
    elif is_tag: # tag 중간에 있는 문자열들
        print(my_str[i], end='') # 그대로 출력
    else: # tag 밖의 상황
        if my_str[i]==' ': # 공백을 만나면
            print_reverse(ans_list) # 기존에 담아 두었던 것 모두 거꾸로 출력
            print(my_str[i], end='') # 공백 그대로 출력
        else: # 공백이 아닌 단어들의 구간이라면
            ans_list.append(my_str[i]) # 뒤집어야 하는 stack에 집어넣기
print_reverse(ans_list) # 마지막에 남아 있는 단어도 출력하기