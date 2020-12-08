a = []
with open('8.txt') as f:
    for line in f:
        a.append(line.rstrip().split(' '))

pos = 0
acc = 0
visited = []

while pos not in visited:
    visited.append(pos)
    if a[pos][0] == 'acc':
        acc += int(a[pos][1])
    elif a[pos][0] == 'jmp':
        pos += int(a[pos][1])
        continue
    pos += 1

print(acc)
