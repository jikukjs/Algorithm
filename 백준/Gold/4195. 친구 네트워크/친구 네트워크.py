def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
    
def union(x,y):
    x_p = find(x)
    y_p = find(y)
    
    if x_p != y_p:
        parent[y_p] = x_p
        num[x_p] += num[y_p]


T = int(input())

for i in range(T):
    parent = dict()
    num = dict()
    N = int(input())
     
    for n in range(N):
        x, y = input().split()
        
        if x not in parent:
            parent[x] = x
            num[x] =1
            
        if y not in parent:
            parent[y] = y
            num[y] =1
    
        union(x,y)
        print(num[find(x)])