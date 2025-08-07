result = 0
cnt = 1

n = int(input())

while(n>0):
    if n >= cnt:
        n-=cnt
        cnt+=1
    
    else:
        cnt = 1
        n-=cnt
        cnt +=1 
    result+=1

print(result)  