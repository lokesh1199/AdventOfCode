def check(buses, startTime):
    for pos in buses:
        if not (startTime + pos) % buses[pos] == 0:
            return False
    return True


def getTime(busID, startTime=0):
    i = startTime
    while True:
        if i % busID == 0:
            return i
        i += 1


with open('13.txt') as f:
    a = f.readlines()[1]
    buses = {}
    for count, bus in enumerate(a.split(',')):
        if bus != 'x':
            buses[count] = int(bus)

time = 0
i = getTime(buses[0], 100000000000000)
while not time:
    print('\r' + str(i), end='', flush=True)
    for pos in buses:
        if i % buses[pos] == 0 and check(buses, i):
            time = i
        else:
            break
    i += buses[0]
