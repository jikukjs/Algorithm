import sys

input = sys.stdin.readline

def join(x,y):
    x_p = find(x)
    y_p = find(y)
    
    
    if x_p < y_p:    
        parents[y_p] = x_p
    else :
        parents[x_p] = y_p
        

def find(x):
    if x == parents[x]:
        return x
    else :
        parents[x] = find(parents[x])
        return parents[x]

n, m = map(int, input().split())

parents = []
check = 0

for i in range(n):
    parents.append(i)

for j in range(m):
    x, y = map(int, input().split())
    
    if find(x) == find(y):
        check =1
        print(j+1)
        break
    else :
        join(x,y)
  
if not check:
    print(0)