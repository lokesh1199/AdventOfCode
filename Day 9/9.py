with open('9.txt') as f:
    a = [int(i.rstrip()) for i in f]


def check(a, x, pos, n):
    a = a[pos-n:pos]
    for i, j in enumerate(a):
        for k in a[i+1:]:
            if j+k == x:
                return True
    return False


i = 25
while i < len(a):
    if not check(a, a[i], i, 25):
        print(a[i])
    i += 1
