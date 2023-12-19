from pprint import pprint
import re
from tqdm import tqdm

f = "day_19/day19_input.txt"
with open(f, 'r') as file:
    lines = file.read().split("\n\n")

def evaluate_condition(conditions):
    for c in conditions["c"]: # c is [condition, target] so c[0][0] is the xmas letter
        match = re.match(r"[a-z]([<>])(\d+)", c[0])
        if match:
            operator, value_str = match.groups()
            value = int(value_str)
            workflows[c[1]]["xmas"] = conditions["xmas"]
            if operator == '<':
                workflows[c[1]]["xmas"][c[0][0]][1] = value - 1
            elif operator == '>':
                workflows[c[1]]["xmas"][c[0][0]][0] = value + 1
            to_visit.append(c[1])
        elif c[0] == 'else':
            if c[1] == 'A':
                combos += mul(xmas.values())
            elif c[1] != 'R':
                to_visit.append(c[1])
    return

workflows = {}
xmas_fsr = {"x": [1, 4001], "m": [1, 4001], "a": [1, 4001], "s": [1, 4001]}
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
    workflows[key] = {"c": conditions, "xmas": xmas_fsr}

combos = 0
to_visit = ['in']
while to_visit != []:
    workflow = to_visit.pop()
    print(workflow)
    i = 0
    evaluate_condition(workflows[workflow])
print(combos)