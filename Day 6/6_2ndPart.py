def solve(ans):
    a = [chr(i) for i in range(97, 123)]
    for i in ans:
        a = [j for j in i if j in a]
    return len(a)


with open('6.txt') as f:
    a = f.readlines()

a = ''.join(a)
a = a.split('\n\n')

count = 0
for i in a:
    count += solve(i.split('\n'))
print(count)
