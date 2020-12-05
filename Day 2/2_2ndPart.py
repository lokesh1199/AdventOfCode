def solve():

    res = 0
    a = []
    with open('2.txt') as f:
        for line in f:
            a.append(line.strip())

    for line in a:
        line = line.split('-')
        index1 = int(line[0]) - 1
        line = line[1].split(' ')
        index2 = int(line[0]) - 1

        policy = line[1][:-1]
        password = line[2]

        if (password[index1] == policy and password[index2] != policy) or (password[index1] != policy and password[index2] == policy):
            res += 1
            print(password)

    return res


print(solve())
