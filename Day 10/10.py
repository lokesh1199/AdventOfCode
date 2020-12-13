with open('10.txt') as f:
    a = [int(i.rstrip()) for i in f]

a.append(0)  # the charging outlet effective rating
a.sort()
a.append(a[-1]+3)  # for your device builtin adapter

c3 = c1 = 0
for i, j in enumerate(a[:-1]):
    if j+1 == a[i+1]:
        c1 += 1
    else:
        c3 += 1

print(c1*c3)
