def sum_four_num(r, c):
    return int(matrix[0][c]) + int(matrix[6][c]) + int(matrix[r][0]) + int(matrix[r][6])


players = input().split(', ')

matrix = []

for _ in range(7):
    matrix.append([x for x in input().split()])

turns, score = {}, {}

turns[players[0]], turns[players[1]] = 0, 0
score[players[0]], score[players[1]] = 501, 501

while True:
    turns[players[0]] += 1

    row, col = [int(x) for x in input().strip('(').strip(')').split(', ')]

    if row >= 7 or row < 0 or col >= 7 or col < 0:
        players[0], players[1] = players[1], players[0]
        continue

    elif matrix[row][col].isdigit():
        score[players[0]] -= int(matrix[row][col])
    elif matrix[row][col] == 'D':
        get_sum = sum_four_num(row, col) * 2
        score[players[0]] -= get_sum
    elif matrix[row][col] == 'T':
        get_sum = sum_four_num(row,col) * 3
        score[players[0]] -= get_sum
    elif matrix[row][col] == 'B':
        print(f"{players[0]} won the game with {turns[players[0]]} throws!")
        break
    if score[players[0]] <= 0:
        print(f"{players[0]} won the game with {turns[players[0]]} throws!")
        break

    players[0], players[1] = players[1], players[0]