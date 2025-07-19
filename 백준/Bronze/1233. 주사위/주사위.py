A,B,C = list(map(int,input().split()))

total = A+B+C
sum = 0

cnt_list = [0]*(total+1)

for a in range(1,A+1):
    for b in range(1,B+1):
        for c in range(1,C+1):     
            sum = a+b+c
            cnt_list[sum]+=1
        

print(cnt_list.index(max(cnt_list)))