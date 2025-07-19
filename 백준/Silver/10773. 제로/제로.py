N = int(input())
sum_list = []

for _ in range(N):
    n = int(input())
    
    if n:
        sum_list.append(n)
    else :
        sum_list.pop()
        
print(sum(sum_list))