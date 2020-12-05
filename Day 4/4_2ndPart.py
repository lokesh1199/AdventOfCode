import string


def check(passport, reqFields):
    passport = passport.replace('\n', ' ').split(' ')
    fields = [i.split(':')[0] for i in passport]
    val = [i.split(':')[1] for i in passport]
    passport = dict(zip(fields, val))

    for reqField in reqFields:
        if reqField not in fields:
            return 0
        else:
            if reqField == 'byr':
                tmp = int(passport[reqField])
                if not (tmp >= 1920 and tmp <= 2002):
                    return 0
            elif reqField == 'iyr':
                tmp = int(passport[reqField])
                if not (tmp >= 2010 and tmp <= 2020):
                    return 0
            elif reqField == 'eyr':
                tmp = int(passport[reqField])
                if not (tmp >= 2020 and tmp <= 2030):
                    return 0
            elif reqField == 'hgt':
                hgt, unit = int(passport[reqField][:-2]
                                ), passport[reqField][-2:]
                if unit == 'cm':
                    if not (hgt >= 150 and hgt <= 193):
                        return 0
                elif unit == 'in':
                    if not (hgt >= 59 and hgt <= 76):
                        return 0
                else:
                    return 0
            elif reqField == 'hcl':
                hcl = passport[reqField]
                if not (hcl[0] == '#' and all(c in string.hexdigits for c in hcl[1:])):
                    return 0
            elif reqField == 'ecl':
                ecl = passport[reqField]
                if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    return 0
            elif reqField == 'pid':
                pid = passport[reqField]
                if not (len(pid) == 9 and pid.isnumeric()):
                    return 0
    return 1


with open('4.txt') as f:
    passports = f.readlines()
passports = ''.join(passports)
passports = passports.split('\n\n')

reqFields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
validPassports = 0

for passport in passports:
    if check(passport, reqFields):
        validPassports += 1
print(validPassports)
