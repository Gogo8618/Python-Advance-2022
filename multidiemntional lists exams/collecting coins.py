def get_next_step(direction, r, c):
    if direction == 'up':
        if r - 1 < 0:
            r = n - 1
        else:
            r -= 1
    elif direction == 'down':
        if r + 1 >= n:
            r = 0
        else:
            r += 1
    elif direction == 'left':
        if c - 1 < 0:
            c = n - 1
        else:
            c -= 1
    elif direction == 'right':
        if c + 1 >= n:
            c = 0
        else:
            c += 1
    return r, c


n = int(input())

matrix = []
row, col = 0, 0
coins = 0
path = []
is_won = False
for i in range(n):
    matrix.append([x for x in input().split()])
    for j in range(n):
        if matrix[i][j] == 'P':
            row, col = i, j

while not is_won:
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
            is_won = True

if not is_won:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for i in path:
    print(i)
