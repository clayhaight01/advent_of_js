from pprint import pprint
f = "day_18/day18_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()

directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

pos = [[0,0]]
allpos = []
dirs = []
lens = []
colors = []
for line in lines:
    line = line.split(" ")
    dirs.append(line[0])
    lens.append(int(line[1]))
    colors.append(line[2])
for i in range(len(dirs)):
    pos.append([pos[i][0] + directions[dirs[i]][0] * lens[i], pos[i][1] + directions[dirs[i]][1] * lens[i]])

for i in range(len(pos) - 1):
    start = pos[i]
    end = pos[i + 1]
    if start[0] == end[0]:  # Vertical movement
        step = 1 if start[1] < end[1] else -1
        for y in range(start[1], end[1], step):
            allpos.append([start[0], y])
    else:  # Horizontal movement
        step = 1 if start[0] < end[0] else -1
        for x in range(start[0], end[0], step):
            allpos.append([x, start[1]])
print(allpos)
up = min([pos[i][1] for i in range(len(pos))])
down = max([pos[i][1] for i in range(len(pos))])
left = min([pos[i][0] for i in range(len(pos))])
right = max([pos[i][0] for i in range(len(pos))])

map = [["." for i in range(left, right+1)] for j in range(up, down+1)]
for p in allpos:
    map[p[1]-up][p[0]-left] = "#"
pprint(map)

area = 0
for i in range(up, down+1):
    width = [p[0] for p in allpos if p[1] == i]
    print(width)
    i = 1
    while abs(width[i] - width[i-1] == -1):
        i += 1
'''
I want to find gaps in the width list, and then calculate the area of the rectangle
'''
print(area)