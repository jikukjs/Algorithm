key_num = int(input())
for n in range(key_num):
    key = input()
    left_key = []
    right_key = []

    for w in key:
        if w == '<':
            if left_key:
                right_key.append(left_key.pop())
        elif w == '>':
            if right_key:
                left_key.append(right_key.pop())
        elif w == '-':
            if left_key:
                left_key.pop()
        else :
            left_key.append(w)

    left_key.extend(reversed(right_key))
    print(''.join(left_key))