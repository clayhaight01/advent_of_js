f = "day_09/day9_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()

sum = 0
for line in lines:
    seq = list(map(int, line.strip().split(' ')))
    d = []
    d.append(seq)
    r = 0
    while not all(v == 0 for v in d[-1]):
        d.append([0] * len(seq))
        for i in range(len(seq)-1-r):
            d[-1][i] = d[r][i+1]-d[r][i]
        r += 1
    for v in d:
        v.append(0)
    for i in range(2,len(d)+1):
        d[-i][len(d[0])-len(d)+i-1] = d[-i][len(d[0])-len(d)+i-2] + d[-i+1][len(d[0])-len(d)+i-2]
    for j in d:
        sum += j[-1]
print(sum)

