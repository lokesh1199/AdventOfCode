def solve(right, down):
    res = 0
    with open('3.txt') as f:
        posX = 0
        posY = 0
        a = f.readlines()
        width = len(a[0])-1
        while posY < len(a):
            if a[posY].rstrip()[posX] == '#':
                res += 1
            posX = (posX+right) % width
            posY += down
    return res


#  slopes = (right, down)
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
res = 1
for slope in slopes:
    res *= solve(*slope)
print(res)
