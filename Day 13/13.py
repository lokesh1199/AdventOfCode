with open('13.txt') as f:
    a = f.readlines()

time = int(a[0])
buses = []
for bus in a[1].split(','):
    if bus != 'x':
        buses.append(int(bus))

i = time
resBus = 0
while not resBus:
    for bus in buses:
        if i % bus == 0:
            resBus = bus
    i += 1

print(resBus * (i - 1 - time))
