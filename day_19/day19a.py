from pprint import pprint
import re
f = "day_19/day19_input.txt"
with open(f, 'r') as file:
    lines = file.read().split("\n\n")

def evaluate_condition(condition_pair, xmas):
    match = re.match(r"[a-z]([<>])(\d+)", condition_pair[0])
    if match:
        operator, value_str = match.groups()
        value = int(value_str)
        n = xmas[condition_pair[0][0]]
        if (operator == '<' and n < value) or (operator == '>' and n > value):
            return condition_pair[1]
    elif condition_pair[0] == 'else':
        return condition_pair[1]
    return None

parsed_1 = {}
for line in lines[0].splitlines():
    key, values = line.strip().split("{")
    values = values[:-1]
    conditions = []
    for val in values.split(","):
        if ":" in val:
            condition, targets = val.split(":")
            targets = targets.split(",")[0]
        else:
            condition = "else"
            targets = val.split(",")[0]

        conditions.append([condition, targets])
    parsed_1[key] = conditions

tsum = 0
for line in lines[1].splitlines():
    workflow = 'in'
    values = re.findall(r"(\w+)=(\d+)", line)
    xmas = {key: int(value) for key, value in values}
    print(xmas)
    i = 0
    while workflow != 'A' and workflow != 'R':
        temp = evaluate_condition(parsed_1[workflow][i], xmas)
        if temp is not None:
            workflow = temp
            i = 0
        else:
            i+=1
        print(workflow)
    if workflow == 'A':
        print("accepted")
        tsum += sum(xmas.values())
    else:
        print("rejected")
print(tsum)