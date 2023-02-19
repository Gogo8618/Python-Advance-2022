def get_next_movie(direction, r, c):
    if direction == 'up':
        r -= 1
    elif direction == 'down':
        r += 1
    elif direction == 'left':
        c -= 1
    elif direction == 'right':
        c += 1
    return r, c


n = int(input())
field = []
row_ = 0
col_ = 0
bombs = 0
cruisers = 0
for row in range(n):
    field.append([x for x in input()])
    for col in range(n):
        if field[row][col] == 'S':
            row_, col_ = row, col

while True:
    command = input()

    next_row, next_col = get_next_movie(command, row_, col_)

    if field[next_row][next_col] == '*':
        field[row_][col_] = '-'
        row_, col_ = next_row, next_col
        field[row_][col_] = 'S'
        bombs += 1
    elif field[next_row][next_col] == 'C':
        field[row_][col_] = '-'
        row_, col_ = next_row, next_col
        field[row_][col_] = 'S'
        cruisers += 1
    elif field[next_row][next_col] == '-':
        field[row_][col_] = '-'
        row_, col_ = next_row, next_col
        field[row_][col_] = 'S'
    if bombs == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row_}, {col_}]!")
        break
    elif cruisers == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

for row in field:
    print(''.join(row))
