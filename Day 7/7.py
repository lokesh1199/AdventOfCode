import re


def checkColor(color):
    if color == 'no other':
        return False
    if color in validColors:
        return True
    else:
        for c in rules[color]:
            if checkColor(c):
                validColors.append(color)
                return True


colorReg = re.compile(r'^(\w+ \w+) bags')
containsReg = re.compile(r' (\w+ \w+) bag[s]?')
rules = {}

validColors = ['shiny gold']

with open('7.txt') as f:
    for i in f:
        key = colorReg.search(i).group(1)
        val = containsReg.findall(i)
        rules[key] = val

for color in rules:
    checkColor(color)

print(len(validColors)-1)
