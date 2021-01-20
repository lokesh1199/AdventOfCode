from pprint import pprint
import sys

with open('10.txt') as f:
    a = [int(i.rstrip()) for i in f]

a.append(0)  # the charging outlet effective rating
a.sort()
a.append(a[-1]+3)  # for your device builtin adapter

paths = {}


def checkPath(a, i=0):
    # memoization
    res = paths.get(i)
    if res != None:
        return res

    length = len(a)
    if i == length-1:
        return 1

    valid = (1, 2, 3)
    res = 0
    if i+1 < length and a[i+1] - a[i] in valid:
        res += checkPath(a, i+1)
    if i+2 < length and a[i+2] - a[i] in valid:
        res += checkPath(a, i+2)
    if i+3 < length and a[i+3] - a[i] in valid:
        res += checkPath(a, i+3)

    paths[i] = res
    return res


print(checkPath(a))
