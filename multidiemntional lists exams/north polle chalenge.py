def get_next_position(dir_, n_row, n_col):
    if dir_ == 'up':
        if n_row - 1 < 0:
            n_row = row - 1
        else:
            n_row -= 1
    elif dir_ == 'down':
        if n_row + 1 == row:
            n_row = 0
        else:
            n_row += 1
    elif dir_ == 'left':
        if n_col - 1 < 0:
            n_col = col - 1
        else:
            n_col -= 1
    elif dir_ == 'right':
        if n_col + 1 == col:
            n_col = 0
        else:
            n_col += 1
    return n_row, n_col


row, col = [int(x) for x in input().split(', ')]

matrix = []

player_row = 0
player_col = 0
find_presents = 0

for r in range(row):
    matrix.append([el for el in input().split()])
    for c in range(col):
        if matrix[r][c] == 'Y':
            player_row = r
            player_col = c
        elif matrix[player_row][player_col] in ('D', 'C', 'G'):
            find_presents += 1

presents = {'D': 0, 'G': 0, 'C': 0}

while presents != 0:

    line = input().split('-')
    if line[0] == "End":
        break
    else:

        direction, steps = line[0], int(line[1])
        for i in range(steps):
            next_row, next_col = get_next_position(direction, player_row, player_col)
            if matrix[next_row][next_col] in ('D', 'G', 'C'):
                find_presents -= 1
                presents[matrix[next_row][next_col]] += 1
            matrix[player_row][player_col] = 'x'
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'Y'
            if presents == 0:
                print(f'Merry Christmas!')
                break
print("You've collected:")

for key, value in presents.items():
    if key == 'D':
        print(f"- {value} Christmas decorations")
    elif key == 'G':
        print(f"- {value} Gifts")
    elif key == 'C':
        print(f"- {value} Cookies")

for row in matrix:
    print(*row)
