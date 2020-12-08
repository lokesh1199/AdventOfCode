def check(a):
    acc = 0
    pos = 0
    visited = []
    while pos < len(a):
        visited.append(pos)
        if a[pos][0] == 'acc':
            acc += int(a[pos][1])
        elif a[pos][0] == 'jmp':
            tmp = pos + int(a[pos][1])
            if tmp in visited:
                return None
            else:
                pos = tmp
            continue
        pos += 1
    return acc


a = []
with open('8.txt') as f:
    for line in f:
        a.append(line.rstrip().split(' '))

for i, line in enumerate(a):
    if line[0] == 'nop':
        tmp = check(a[:i] + [['jmp', line[1]]] + a[i+1:])
        if tmp:
            print(tmp)
    elif line[0] == 'jmp':
        tmp = check(a[:i] + [['nop', line[1]]] + a[i+1:])
        if tmp:
            print(tmp)
            break
