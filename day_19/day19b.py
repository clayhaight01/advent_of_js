import re
import math
from pprint import pprint

f = "day_19/day19_input.txt"
with open(f, 'r') as file:
    lines = file.read().split("\n\n")

class Workflow:
    def __init__(self, name, conditions, xmas={'x': [1, 4000],'m': [1, 4000],'a': [1, 4000],'s': [1, 4000]}):
        self.name = name
        self.conditions = conditions
        self.children = []
        self.xmas = xmas
        self.combos = 0

    def add_child(self, child):
        self.children.append(child)

    def calculate_combos(self):
        if any(self.xmas[key][0] > self.xmas[key][1] for key in self.xmas):
            self.combos = 0
        else:
            self.combos = math.prod([self.xmas[key][1] - self.xmas[key][0] + 1 for key in self.xmas])

    def split_range(self, rule, xmas):
        match = re.match(r"[a-z]([<>])(\d+)", rule)
        if match:
            operator, value_str = match.groups()
            value = int(value_str)
            xmas_char = rule[0]
            if operator == '<':
                xmas[xmas_char][1] = value - 1
            elif operator == '>':
                xmas[xmas_char][0] = value + 1
        return xmas
    
    def recurse(self):
        path_combos = 0
        if self.name == "A":
            self.calculate_combos()
            return self.combos
        elif self.name == "R":
            self.combos = 0
            return 0
        
        for condition in self.conditions:
            split_xmas = {k: v[:] for k, v in self.xmas.items()}
            split_xmas = self.split_range(condition[0], split_xmas)
            if condition[1] != "A" and condition[1] != "R":
                self.add_child(Workflow(condition[1], workflows[condition[1]], split_xmas))
            else:
                self.add_child(Workflow(condition[1], None, split_xmas))
        for child in self.children:
            path_combos += child.recurse()
        return path_combos
    
    def __str__(self, depth=0):
        indent = "  " * depth
        result = f"{indent}{self.name}, Conditions: {self.conditions}, Xmas: {self.xmas}, Combos: {self.combos}\n"
        for child in self.children:
            result += child.__str__(depth + 1)
        return result
    
    def get_ranges(self):
        result = []
        if self.name == "A":
            result.append(self.xmas)
            return result
        for child in self.children:
            result += child.get_ranges()
        return result
    
def filter_ranges(ranges):
    
    return 

workflows = {}
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
    workflows[key] = conditions

start = 'in'
root_workflow = Workflow(start, workflows[start])
total_combos = root_workflow.recurse()
ranges = root_workflow.get_ranges()
pprint(ranges)
print(root_workflow)
print(f"Total combos: {total_combos}")
