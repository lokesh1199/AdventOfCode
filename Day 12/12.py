with open('12.txt') as f:
    a = [(line[0], int(line[1:].rstrip())) for line in f]

directions = ['E', 'S', 'W', 'N']
cords = dict.fromkeys(directions, 0)
curr = 0

for ins in a:
    if ins[0] == 'F':
        cords[directions[curr]] += ins[1]
        cords[directions[(curr+2) % len(directions)]] -= ins[1]
    elif ins[0] == 'R':
        i = ins[1] / 90
        curr = int((curr+i) % len(directions))
    elif ins[0] == 'L':
        i = (360 - ins[1]) / 90
        curr = int((curr + i) % len(directions))
    else:
        cords[ins[0]] += ins[1]
        opposite = directions[(directions.index(
            ins[0])+2) % len(directions)]
        cords[opposite] -= ins[1]

a = max(cords[directions[0]], cords[directions[2]])
b = max(cords[directions[1]], cords[directions[3]])
print(a+b)
