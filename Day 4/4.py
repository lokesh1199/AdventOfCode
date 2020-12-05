def check(passport, reqFields):
    passport = passport.replace('\n', ' ').split(' ')
    fields = [i.split(':')[0] for i in passport]

    for reqField in reqFields:
        if reqField not in fields:
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
