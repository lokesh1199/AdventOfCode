class Ship:
    directions = ['N', 'E', 'S', 'W']
    oppDirections = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, waypoint):
        self.waypoint = dict(zip(Ship.directions, waypoint))
        self.position = dict(zip(Ship.directions, [0, 0, 0, 0]))
        self.waypointDir = [0, 1]

    def forward(self, x):
        for key in self.waypoint:
            if key in self.getWaypointDir():
                currDir = self.waypoint[key] * x
                oppDir = x * self.waypoint[Ship.oppDirections[key]]
                self.position[key] += currDir - oppDir

    def rotate(self, angle):
        val = []
        for dir in Ship.directions:
            val.append(self.waypoint[dir])

        if angle < 0:
            angle = abs(angle)
            i = 1
        else:
            i = -1

        rotations = angle // 90
        for _ in range(rotations):
            val = val[i:] + val[:i:]

        self.waypoint = dict(zip(Ship.directions, val))
        tmp = self.waypointDir
        tmp[0] = (tmp[0]+rotations) % len(Ship.directions)
        tmp[1] = (tmp[1]+rotations) % len(Ship.directions)
        self.waypointDir = tmp

    def north(self, x):
        self.waypoint['N'] += x

    def south(self, x):
        self.waypoint['S'] += x

    def east(self, x):
        self.waypoint['E'] += x

    def west(self, x):
        self.waypoint['W'] += x

    def getWaypointDir(self):
        return (
            Ship.directions[self.waypointDir[0]],
            Ship.directions[self.waypointDir[1]]
        )

    def manhattanDistance(self):
        return (
            abs(self.position['N'] - self.position['S']) +
            abs(self.position['E'] - self.position['W'])
        )


with open('12.txt') as f:
    a = [(line[0], int(line[1:].rstrip())) for line in f]

s = Ship([1, 10, 0, 0])

for instr in a:
    cmd, val = instr
    if cmd == 'F':
        s.forward(val)
    elif cmd == 'L':
        s.rotate(-1 * val)
    elif cmd == 'R':
        s.rotate(val)
    elif cmd == 'N':
        s.north(val)
    elif cmd == 'S':
        s.south(val)
    elif cmd == 'W':
        s.west(val)
    elif cmd == 'E':
        s.east(val)
print(s.manhattanDistance())
