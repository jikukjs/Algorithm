from collections import deque


N, L, W = map(int, input().split())

Check = deque()
truck = deque(map(int, input().split()))
cnt =0 

while(truck):
    t = truck.popleft()
    if Check:
        if len(Check) == L:
            Check.popleft()
            if sum(Check)+t <= W:
                Check.append(t)
            else :
                Check.append(0)
                truck.appendleft(t)
        else:
            if sum(Check)+t <= W:
                Check.append(t)
            else :
                Check.append(0)
                truck.appendleft(t)
            
    else:
        Check.append(t)
        
    cnt+=1
    
print(cnt+L)