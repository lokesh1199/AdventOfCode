def solve():
    res = 0
    with open('3.txt') as f:
        pos = 0
        width = 31
        for line in f:
            if line.rstrip()[pos] == '#':
                res += 1
            pos = (pos+3) % width
    return res


print(solve())
