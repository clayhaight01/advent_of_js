f = "day_06/day6_input.txt"
lines = open(f).read().splitlines()

time_data = list(map(int, lines[0].split()[1:]))
distance_data = list(map(int, lines[1].split()[1:])) 
tds = list(zip(time_data, distance_data))

num_ways = []
for td in tds:
    ways = 0
    for v in range(td[0]+1):
        d = v*(td[0]-v)
        if d > td[1]:
            ways += 1
    num_ways.append(ways)
print(num_ways)
result = 1
for val in num_ways:
    result *= val
print(result)