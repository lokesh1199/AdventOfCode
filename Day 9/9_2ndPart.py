def check(a, x, pos, n):
    a = a[pos-n:pos]
    for i, j in enumerate(a):
        for k in a[i+1:]:
            if j+k == x:
                return True
    return False


def findSum(a, i, n):
    sum = largest = smallest = a[i]
    for j in a[i+1:]:
        sum += j
        largest = largest if largest > j else j
        smallest = smallest if smallest < j else j
        if sum == n:
            return smallest + largest
        elif sum > n:
            return None


with open('9.txt') as f:
    a = [int(i.rstrip()) for i in f]

i = 25
res = None
while i < len(a):
    if not check(a, a[i], i, 25):
        res = a[i]
        break
    i += 1

a = a[:i]

for i, j in enumerate(a):
    tmp = findSum(a, i, res)
    if tmp:
        print(tmp)
        break
