import math

with open("day_04/day4_input.txt", 'r') as file:
    characters_array = [line.strip() for line in file]

sum = 0
for row in characters_array:
    split_array = row.split('|')
    winning = [int(num) for num in split_array[0].split() if num.isdigit()]
    ours = [int(num) for num in split_array[1].split() if num.isdigit()]
    num_wins = 0
    for num in ours:
        if num in winning:
            num_wins += 1
    sum += math.floor(2**(num_wins-1))
print(sum)

