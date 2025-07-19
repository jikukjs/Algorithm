N = int(input())

n_list = list(map(int,input().split()))
stack= []
ngv=[-1]*N

for i in range(N):
    
    if (len(stack)==0 or stack[-1][0]>=n_list[i]):
        stack.append((n_list[i],i))
    else:
        while(len(stack)>0):
            if stack[-1][0] < n_list[i]:
                x = stack.pop()
                ngv[x[1]]= n_list[i]
            else:
                break
        stack.append((n_list[i],i))
        
for x in ngv:
    print(x, end=' ')