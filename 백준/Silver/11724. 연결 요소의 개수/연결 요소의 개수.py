import sys
input = sys.stdin.readline

def find_set(set_list,x):
    if set_list[x] != x:
        set_list[x] = find_set(set_list,set_list[x])
    return set_list[x]

def union_set(set_list,x,y):
    x = find_set(set_list,x) 
    y = find_set(set_list,y) 

    if x<y:
        set_list[y] = x
    else:
        set_list[x] = y

N,M = list(map(int,input().split()))
set_list = [0]*(N+1)

for i in range(1,N+1):
    set_list[i] = i

for _ in range(M):
    a,b = map(int,input().split()) 
    union_set(set_list,a,b)

set_set = set()
for i in range(1,N+1):
    set_set.add(find_set(set_list,i))
print(len(set_set))