f = "day_07/day7_input.txt"
with open(f, 'r') as file:
    lines = file.read().splitlines()

directions = list(lines[0])

node_dict = {}
curr_nodes = []
end_nodes = []

for line in lines[2:]:
    key, values = line.strip().split(' = ')
    values = tuple(values.strip('()').split(', '))
    
    node_dict[key.strip()] = values
    if list(key)[2] == 'A':
        curr_nodes.append(key)
    elif list(key)[2] == 'Z':
        end_nodes.append(key)

steps = 0
LCM_dict = {}
print(curr_nodes)

def lcms(curr_nodes):
    prev = True
    for node in curr_nodes:
        if node[2] == 'Z':
            if node not in LCM_dict:
                LCM_dict[node] = [steps,0]
            else:
                LCM_dict[node][1] = steps
    if len(LCM_dict)>0:
        done = True
        for node in LCM_dict:
            done = done and LCM_dict[node][1] != 0
        return done
    return False

while not lcms(curr_nodes) and steps < 50000000000:
    if directions[0] == 'L':
        for n in range(len(curr_nodes)):
            curr_nodes[n] = node_dict[curr_nodes[n]][0]
    else:
        for n in range(len(curr_nodes)):
            curr_nodes[n] = node_dict[curr_nodes[n]][1]
    # print(curr_nodes)
    fdir = directions.pop(0)
    directions.append(fdir)
    steps += 1

paths = [] * len(LCM_dict)
for o in LCM_dict:
    paths.append(o[0])
print(paths)
# while paths.count(paths[0]) != len(LCM_dict):
#     for p in paths:
#         print(p)

print(LCM_dict)
