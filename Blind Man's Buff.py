def get_next_move(direction, r, c):
    if direction == 'up':
        if r - 1 < 0:
            r = row
        else:
            r -= 1
    elif direction == 'down':
        if r + 1 >= n:
            r = row
        else:
            r += 1
    elif direction == 'left':
        if c - 1 < 0:
            c = col
        else:
            c -= 1
    elif direction == 'right':
        if c + 1 >= m:
            c = col
        else:
            c += 1
    return r, c


n, m = [int(x) for x in input().split()]
matrix = []
row, col = 0, 0

touched = 0
moves = 0

for row_ in range(n):
    matrix.append([x for x in input().split()])
    for col_ in range(m):
        if matrix[row_][col_] == 'B':
            row, col = row_, col_

while True:

    if touched == 3:
        break
    command = input()
    if command == 'Finish':
        break
    next_row, next_col = get_next_move(command, row, col)
    if matrix[next_row][next_col] == 'O':
        continue
    elif matrix[next_row][next_col] == '-':
        moves += 1
        matrix[row][col] = '-'
        row, col = next_row, next_col
        matrix[row][col] = 'B'
    elif matrix[next_row][next_col] == 'P':
        touched += 1
        moves += 1
        matrix[row][col] = '-'
        row, col = next_row, next_col
        matrix[row][col] = 'B'


print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")