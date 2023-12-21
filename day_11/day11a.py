from pprint import pprint
f = "day_11/day11_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()
space = [list(line) for line in lines]
gspace = [row[:] for row in space]

itd = 0
for i, r in enumerate(space):
    j = 0
    while r[j] == '.':
        if j == len(r)-1:
            gspace.insert(i+itd+1,list('.'*len(space[0])))
            itd += 1
            break
        j+=1
itd = 0
for ci in range(len(space[0])-1):
    ri = 0
    while space[ri][ci] == '.':
        if ri == len(space)-1:
            for r in gspace:
                r.insert(ci+itd+1,'.')
            itd += 1
            break
        ri+=1

galaxies = []
for i in range(len(gspace)):
    for j in range(len(gspace[0])):
        if gspace[i][j] == '#':
            galaxies.append((i,j))

visited = set()
sum = 0
for i, gax in enumerate(galaxies):
    visited.add(gax)
    for oth in galaxies[i+1:]:
        if oth not in visited:
            sum += abs(oth[0]-gax[0])+abs(oth[1]-gax[1])
print(sum)
