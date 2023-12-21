f = "day_11/day11_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()
space = [list(line) for line in lines]

# Find empty rows and columns
emptyr = [1]*len(space)
emptyc = [1]*len(space[0])
for i, r in enumerate(space):
    j = 0
    while r[j] == '.':
        if j == len(r)-1:
            emptyr[i] = 1000000
            break
        j+=1
for ci in range(len(space[0])-1):
    ri = 0
    while space[ri][ci] == '.':
        if ri == len(space)-1:
            emptyc[ci] = 1000000
            break
        ri+=1

galaxies = []
for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j] == '#':
            galaxies.append((i,j))

visited = set()
dsum = 0
for i, gax in enumerate(galaxies):
    visited.add(gax)
    for oth in galaxies[i+1:]:
        if oth not in visited:
            cl, ch = min(oth[1],gax[1]), max(oth[1],gax[1])
            rl, rh = min(oth[0],gax[0]), max(oth[0],gax[0])
            dsum += sum(emptyr[rl:rh])+sum(emptyc[cl:ch])
print(dsum)
