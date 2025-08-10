N = int(input())

info = []

for n in range(N):
    age, name = input().split()
    info.append((int(age),int(name)))
    
answer = sorted(info, key = lambda x : (x[0],x[1]))
for age, name in answer:
    print( age, name)