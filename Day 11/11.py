from copy import deepcopy


def gen_adjacent_node(matrix, x, y):
    rowLen = len(matrix)
    colLen = len(matrix[0])

    xCord = (1, -1, 0)
    yCord = (1, -1, 0)

    for i in xCord:
        for j in yCord:
            if i == 0 and j == 0:
                continue
            if x+i < rowLen and x+i >= 0 and y+j < colLen and y+j >= 0:
                yield matrix[x+i][y+j]


def occupy(a, b, i, j):
    for node in gen_adjacent_node(a, i, j):
        if node == '#':
            return
    b[i][j] = '#'


def vacate(a, b, i, j):
    count = 0
    for node in gen_adjacent_node(a, i, j):
        if node == '#':
            count += 1
    if count >= 4:
        b[i][j] = 'L'


def printMat(b):
    for i in b:
        for j in i:
            print(j, end=' ')
        print()


with open(f'11.txt') as f:
    a = [list(i.rstrip()) for i in f]


while True:
    b = deepcopy(a)
    for i, line in enumerate(a):
        for j, val in enumerate(line):
            if val == 'L':
                occupy(a, b, i, j)
            elif val == '#':
                vacate(a, b, i, j)
    if a == b:
        break
    a = deepcopy(b)

res = 0
for i in a:
    for j in i:
        if j == '#':
            res += 1
print(res)
