def solve(seatID):
    rows = [0, 127]
    cols = [0, 7]

    for i in seatID[:-3]:
        if rows[0] < rows[1]:
            mid = (rows[0] + rows[1]) // 2
            if i == 'F':
                rows[1] = mid
            elif i == 'B':
                rows[0] = mid+1
        else:
            break

    for i in seatID[-3:]:
        if cols[0] < cols[1]:
            mid = (cols[0] + cols[1]) // 2
            if i == 'L':
                cols[1] = mid
            elif i == 'R':
                cols[0] = mid+1
        else:
            break

    return rows[0], cols[0]


maxID = 0
with open('5.txt') as f:
    for line in f:
        res = solve(line.rstrip())
        resID = res[0] * 8 + res[1]
        if resID > maxID:
            maxID = resID
print(maxID)
