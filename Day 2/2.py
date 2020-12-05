def solve():

    res = 0
    a = []
    with open('2.txt') as f:
        for line in f:
            a.append(line.strip())

    for line in a:
        line = line.split('-')
        lb = int(line[0])
        line = line[1].split(' ')
        ub = int(line[0])

        policy = line[1][:-1]
        password = line[2]

        count = 0
        for c in password:
            if c == policy:
                count += 1
        if count >= lb and count <= ub:
            res += 1

    return res


print(solve())
