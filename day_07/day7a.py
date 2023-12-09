f = "day_07/day7_input.txt"
lines = open(f).read().splitlines()
deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
winnings = 0
rankings = [None]*7

def place_rank(score, bid, hand):
    if rankings[hand] is None:
        rankings[hand] = []
    rankings[hand].append([score, bid])

for line in lines:
    [cards, bid] = line.split(" ")
    bid = int(bid)
    counts = [0] * 13
    score = 0
    for c in cards:
        counts[deck.index(c)] += 1
        score = score * 14 + deck.index(c)

    if 5 in counts:
        place_rank(score, bid, 6)
    elif 4 in counts:
        place_rank(score, bid, 5)
    elif 3 in counts and 2 in counts:
        place_rank(score, bid, 4)
    elif 3 in counts:
        place_rank(score, bid, 3)
    elif counts.count(2) == 2:
        place_rank(score, bid, 2)
    elif 2 in counts:
        place_rank(score, bid, 1)
    else:
        place_rank(score, bid, 0)
print(rankings)
r = 1
for sublist in rankings:
    if sublist is not None:
        sublist.sort(key=lambda x: x[0])
        for sub in sublist:
            print(sub, r)
            winnings += sub[1] * r
            r += 1

print(winnings)

# print(result)