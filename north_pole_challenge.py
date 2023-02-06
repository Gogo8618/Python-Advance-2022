def get_next_step(dir, pos):
    if dir == 'up':
        if pos[0] - 1 < 0:
            pos[0] = row - 1
        else:
            pos[0] -= 1
    elif dir == 'down':
        if pos[0] + 1 == row:
            pos[0] = 0
        else:
            pos[0] += 1
    elif dir == 'left':
        if pos[1] - 1 < 0:
            pos[1] = columns - 1
        else:
            pos[1] -= 1
    elif dir == 'right':
        if pos[1] + 1 == columns:
            pos[1] = 0
        else:
            pos[1] += 1
    return pos


row, columns = [int(x) for x in input().split(', ')]

matrix = []
position = []
presents = 0
decorations = {'D': 0, 'G': 0, 'C': 0}
for r in range(row):
    matrix.append([x for x in input().split()])
    for c in range(columns):
        if matrix[r][c] == 'Y':
            position = [r, c]
        elif matrix[r][c] in ['D', 'G', 'C']:
            presents += 1

while presents != 0:
    command = input().split('-')

    if command[0] == 'End':
        break
    else:
        direction, steps = command[0], int(command[1])

        for i in range(steps):
            next_row, next_col = get_next_step(direction, position)
            if matrix[next_row][next_col] in ['D', 'C', 'G']:
                presents -= 1
                decorations[matrix[next_row][next_col]] += 1
            matrix[position[0]][position[1]] = 'x'
            position[0], position[1] = next_row, next_col
            matrix[position[0]][position[1]] = 'Y'
            if presents == 0:
                print("Merry Christmas!")
                break
print("You've collected:")

for k, v in decorations.items():
    if k == 'D':
        print(f"-{v} Christmas decorations")
    elif k == 'G':
        print(f"-{v} Gifts")
    elif k == 'C':
        print(f"-{v} Cookies")
for row in matrix:
    print(' '.join(row))
