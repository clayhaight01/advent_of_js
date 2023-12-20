import math

f = "day_10/day10_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()
step = {'S': [[1,0],[0,0]], '|': [[0,0],[0,1]], '-': [[1,0],[0,0]], 'L': [[0,-1],[1,0]], 'J': [[0,-1],[-1,0]], '7': [[0,1],[-1,0]], 'F': [[0,1],[1,0]]} # positive is right and down, first val is hit from side, second is hit from top/bottom
plumbing = [list(line) for line in lines]
pos = [[i, j] for i, row in enumerate(plumbing) for j, char in enumerate(row) if char == 'S']
print("start pos: ",pos)
f = 0
hv = 0 

prior_dir = [1, 1]
while not f or plumbing[pos[-1][0]][pos[-1][1]] != 'S' and f < 100:
    cpos = pos[-1] # current position
    dir = step[plumbing[cpos[0]][cpos[1]]][hv] # get next direction based on current direction and current char
    pos.append([cpos[0] + prior_dir[0]*dir[0], cpos[1] + prior_dir[1]*dir[1]]) # add new position to list
    hv = 1 if dir[0] == 0 else 0 # new horizontal/vertical 0 if horizontal, 1 if vertical
    f += 1
    prior_dir[hv] = dir[hv]
    print("dir: ",dir," pos: ",pos[-1], " prior dir: ",prior_dir," char: ", plumbing[pos[-1][0]][pos[-1][1]])
# print(plumbing)
print(int(math.ceil(f/2)))

