first_list = input()
find_list = input()
first_len = len(first_list)
find_len = len(find_list)

cnt = 0
i = 0

while(i <= first_len - find_len):
    if first_list[i:i+find_len] == find_list:
       cnt +=1 
       i+=find_len
       continue
    i+=1
    
print(cnt)