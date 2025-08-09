N = int(input())

info = []

for n in range(N):
    age, name = input().split()
    info.append((int(age),name))
    
answer = sorted(info, key = lambda x : x[0])
for age, name in answer:
    print( age, name)