f = "day_07/day7_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()

directions = list(lines[0])

nodes_dict = {}

for line in lines[2:]:
    key, values = line.strip().split(' = ')
    values = tuple(values.strip('()').split(', '))
    
    nodes_dict[key.strip()] = values

steps = 0
curr_node = 'AAA'
while curr_node != 'ZZZ':
    if directions[0] == 'L':
        curr_node = nodes_dict[curr_node][0]
    else:
        curr_node = nodes_dict[curr_node][1]
    fdir = directions.pop(0)
    directions.append(fdir)
    print(curr_node)
    print(directions)
    steps += 1

print("Directions:", directions)
print("Nodes:", nodes_dict)
print(steps)
