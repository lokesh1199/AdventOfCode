def solve(ans):
    a = dict.fromkeys([chr(i) for i in range(97, 123)], 0)
    count = 0
    for i in ans:
        for j in i:
            if a.get(j) == 0:
                a[j] = 1
                count += 1
    return count


with open('6.txt') as f:
    a = f.readlines()

a = ''.join(a)
a = a.split('\n\n')

count = 0
for i in a:
    count += solve(i.split('\n'))
print(count)
