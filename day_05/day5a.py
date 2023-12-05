f = "day_05/day5_input.txt"
lines = open(f).read().splitlines()
for l, line in enumerate(open(f).read().splitlines()):
    if l == 0:
        line = line.replace("seeds: ", "")
        seeds = list(map(int, line.split()))
    elif line == "":
        continue
    elif not line[0].isdigit():
        i = l
        mapping = []
        next_form = []
        while (i+1) < len(lines) and lines[i+1] != "":
            mapping.append(list(map(int, lines[i+1].split())))
            i += 1

        for s in seeds:
            found = False
            for m in mapping:
                if s in range(m[1], m[1]+m[2]+1) and found == False:
                    next_form.append(m[0]+(s-m[1]))
                    found = True
            if found == False:
                next_form.append(s)
        seeds = next_form
print(min(seeds))
