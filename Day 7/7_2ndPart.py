import re


def countBags(color):
    if color == 'no other':
        return 0

    count = 1
    for c in rules[color]:
        i = int(c[0]) if c[0] else 0
        count += i * countBags(c[1])
    return count


with open('7.txt') as f:
    a = f.readlines()

colorReg = re.compile(r'^(\w+ \w+) bags')
containsReg = re.compile(r'(\d+)? (\w+ \w+) bag[s]?')


rules = {}
for i in a:
    key = colorReg.search(i).group(1)
    val = containsReg.findall(i)
    rules[key] = val

print(countBags('shiny gold')-1)
