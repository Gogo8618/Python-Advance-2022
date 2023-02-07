def get_next_step(direction, r, c):
    if direction == 'up':
        if r - 1 < 0:
            r = number - 1
        else:
            r -= 1
    elif direction == 'down':
        if r + 1 >= number:
            r = 0
        else:
            r += 1
    elif direction == 'right':
        if c + 1 >= number:
            c = 0
        else:
            c += 1
    elif direction == 'left':
        if c - 1 < 0:
            c = number - 1
        else:
            c -= 1
    return r, c


number = int(input())

matrix = []

row = 0
col = 0

is_win = False
coins = 0
path = []
for r in range(number):
    matrix.append([x for x in input().split()])
    for c in range(number):
        if matrix[r][c] == 'P':
            row, col = r, c

while not is_win:
    command = input()

    next_row, next_col = get_next_step(command, row, col)

    if matrix[next_row][next_col] == 'X':
        path.append([row, col])
        if coins > 0:
            coins //= 2
        path.append([next_row, next_col])
        break
    elif matrix[next_row][next_col].isdigit():
        path.append([row, col])
        coins += int(matrix[next_row][next_col])
        matrix[row][col] = '0'
        matrix[next_row][next_col] = 'P'
        row, col = next_row, next_col
        if coins >= 100:
            path.append([row, col])
            is_win = True


if not is_win:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for row in path:
    print(row)
