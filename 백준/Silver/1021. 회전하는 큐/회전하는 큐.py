from collections import deque

circle = deque()

N, M = map(int,input().split())

put_inx = list(map(int,input().split()))

cnt = 0

for i in range(1,N+1):
    circle.append(i)

for n in put_inx:
    pop = circle.popleft()
    while(pop != n):
        if circle.index(n) >= (len(circle)/2):
            circle.appendleft(pop)
            pop = circle.pop()
            cnt+=1
        else:
            circle.append(pop)
            cnt+=1
            pop = circle.popleft()
print(cnt)