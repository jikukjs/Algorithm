from collections import deque

N ,K = map(int, input().split())

cir = deque()
answer= []
for n in range(1, N+1):
    cir.append(n)
    
while cir:
    for _ in range(K-1):
        cir.append(cir.popleft())
    answer.append(cir.popleft())

print('<', end='')

for i in range(len(answer)):
    if i < len(answer)-1:
        print(answer[i], end= ', ')
    else:
        print(answer[i], end="")
        
print('>')