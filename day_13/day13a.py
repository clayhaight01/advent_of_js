f = "day_13/day13_input.txt"
with open(f, 'r') as file:
    patterns = file.read().split("\n\n")

def locate_reflection(p):
    matches = []
    for r in p:
        m = []
        rr = r.copy()
        rr.reverse()
        for i in range(len(r)): # shifts
            j = 0
            while j < len(r)-i and r[j] == rr[i+j]:
                j += 1
            if j == len(r)-i and i<len(r):
                # print(r,"\n","    "*i,rr,"\n",i)
                m.append(len(r)//2+j-1)
        matches.append(m)
    print(matches)
    matches_set = set(matches[0])
    for lst in matches[1:]:
        matches_set.intersection_update(lst)
    return matches_set

csum = 0
for pattern in patterns:
    print("new pattern")
    p = [list(line) for line in pattern.splitlines()]
    mirrorh = locate_reflection(p)
    print(mirrorh)
    csum += next(iter(mirrorh))
    if len(mirrorh) == 0:
        tp = [list(row) for row in zip(*p)]
        csum += 100*next(iter(locate_reflection(tp)))
print(csum)

            