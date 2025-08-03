
from collections import deque
N = int(input())

move = deque(map(int,input().split()))

result =[]

for i in range(N):
    move[i] = (move[i],i+1)
    
while(move):
    direct, num =move.popleft()
    result.append(num)
    if not move:
        break
    
    if direct > 0:
        for _ in range(direct-1):
            move.append(move.popleft())
    else :
        for _ in range(abs(direct)):
            move.appendleft(move.pop())

for r in result:
    print(r, end=" ")
