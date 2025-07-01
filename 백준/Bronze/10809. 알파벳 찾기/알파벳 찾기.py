my_str = input()
result = [-1]*26
for i in range(len(my_str)):
    index = ord(my_str[i])-ord('a')
    if result[index] == -1:
        result[index] = i
for x in result:
    print(x,end=' ')