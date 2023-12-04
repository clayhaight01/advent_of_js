import math

with open("day_04/day4_input.txt", 'r') as file:
    characters_array = [line.strip() for line in file]

asum = 0
multiplier = [1] * len(characters_array)
for r, row in enumerate(characters_array):
    split_array = row.split('|')
    winning = [int(num) for num in split_array[0].split() if num.isdigit()]
    ours = [int(num) for num in split_array[1].split() if num.isdigit()]
    num_wins = 0
    for num in ours:
        if num in winning:
            num_wins += 1
    for i in range(num_wins):
        multiplier[i+r+1] += multiplier[r]
    print(multiplier)
print(sum(multiplier))

