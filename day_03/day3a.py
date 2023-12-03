# I am so sick of JS already I just want to submit something
with open("day3_input.txt", 'r') as file:
    characters_array = [line.strip() for line in file]

rows = len(characters_array)
cols = len(characters_array[0]) if rows else 0
visited = [[False for _ in row] for row in characters_array]
sum = 0
for i, r in enumerate(characters_array):
    for j, v in enumerate(r):
            if v.isdigit() and not visited[i][j]:
                pn = False
                for x in range(max(0, i-1), min(i+2, rows)):
                    for y in range(max(0, j-1), min(j+2, cols)):
                         if not characters_array[x][y].isdigit() and characters_array[x][y] != '.':
                            pn = True
                if pn:
                    j_temp = j
                    while j_temp > 0 and r[j_temp-1].isdigit():
                        j_temp -= 1
                    pnum = int(r[j_temp])
                    visited[i][j_temp] = True
                    while j_temp + 1 < cols and r[j_temp+1].isdigit():
                        j_temp += 1
                        pnum = pnum * 10 + int(r[j_temp])
                        visited[i][j_temp] = True
                        
                    sum += pnum
print(sum)