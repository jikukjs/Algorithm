n = int(input())
n_list = set(map(int,input().split()))
m = int(input())
m_list=list(map(int,input().split()))

for w in m_list:
    if w in n_list:
        print("1")
    else :
        print("0")