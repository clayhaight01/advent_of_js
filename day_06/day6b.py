t, d = (int(line.split(":")[1].replace(" ","")) for line in open("day_06/day6_input.txt").read().splitlines())
print(sum(1 for v in range(t+1) if v * (t - v) > d))