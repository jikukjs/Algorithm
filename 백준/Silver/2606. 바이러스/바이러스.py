def find(a):
    if linking[a] == a:
        return a
    else :
        parent = find(linking[a])
        linking[a] = parent
        return linking[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a ==1:
        linking[b] = a

    else :
        linking[a] = b

V = int(input())
E = int(input())
linking =[]
cnt = 0

for i in range (V+1):
    linking.append(i)

for _ in range (E):
    a, b = map(int,input().split())
    union(a,b)
    
for i in range(2,V+1):
    if find(i) ==1:
        cnt += 1

print(cnt)