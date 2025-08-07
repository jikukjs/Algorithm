def ascending(tropys):
    now = tropys[0]
    result = 1
    
    for i in range(1, len(tropys)):
        if now < tropys[i]:
            result +=1
            now = tropys[i]
    return result
    
n = int(input())
tropys = []

for _ in range(n):
    tropy = int(input())
    
    tropys.append(tropy)

print(ascending(tropys))
tropys.reverse()
print(ascending(tropys))