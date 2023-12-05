f = "day_05/day5_input.txt"
lines = open(f).read().splitlines()
seeds = []
for l, line in enumerate(open(f).read().splitlines()):
    if l == 0:
        line = line.replace("seeds: ", "")
        preseed = list(map(int, line.split()))
        for r in range(0, len(preseed), 2):
            seeds.append([preseed[r],preseed[r+1]+preseed[r]-1])
    elif line == "":
        continue
    elif not line[0].isdigit():
        i = l
        mapping = []
        next_form = []
        while (i+1) < len(lines) and lines[i+1] != "":
            mapping.append(list(map(int, lines[i+1].split())))
            i += 1
        mapping = sorted(mapping, key=lambda x: x[1])
        for s in seeds:
            f = s.copy() # range left to find
            for m in mapping:
                mstart = m[1]
                mend = m[1]+m[2]-1
                shift = m[0]-m[1]
                n = [0,0]
                
                if f[0] < mstart:
                    if f[1] < mstart:
                        next_form.append([f[0], f[1]])
                        break
                    if f[1] < mend:
                        next_form.append([f[0], mstart-1])
                        next_form.append([m[0], f[1]-mstart+1])
                        break
                    next_form.append([f[0], mstart-1])
                    next_form.append([m[0], m[0]+m[2]])
                    f[0] = mend+1
                elif f[0] <= mend:
                    if f[1] <= mend:
                        next_form.append([f[0]+shift, f[1]+shift])
                        break
                    next_form.append([f[0]+shift, m[0]+m[2]])
                    f[0] = mend+1
            if f[0] > mend:
                next_form.append([f[0], f[1]])

        seeds = next_form
min_value = sorted(seeds, key=lambda x: x[0])[0][0]
print(min_value)
