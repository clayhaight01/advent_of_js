with open("day3_input.txt", 'r') as file:
    characters_array = [line.strip() for line in file]

rows = len(characters_array)
cols = len(characters_array[0]) if rows else 0
visited = [[False for _ in row] for row in characters_array]
sum = 0
for i, r in enumerate(characters_array):
    for j, v in enumerate(r):
            if v == '*':
                ratio = 0;
                for x in range(max(0, i-1), min(i+2, rows)):
                    for y in range(max(0, j-1), min(j+2, cols)):
                        if characters_array[x][y].isdigit() and not visited[x][y]:
                            j_temp = y
                            while j_temp > 0 and characters_array[x][j_temp-1].isdigit():
                                j_temp -= 1
                            pnum = int(characters_array[x][j_temp])
                            visited[x][j_temp] = True
                            while j_temp + 1 < cols and characters_array[x][j_temp+1].isdigit():
                                j_temp += 1
                                pnum = pnum * 10 + int(characters_array[x][j_temp])
                                visited[x][j_temp] = True
                            if ratio > 0:
                                sum += pnum * ratio
                            ratio = pnum
print(sum)