def get_next_steps(row, col, dir, steps_):
    if dir == 'up':
        return row - steps_, col
    if dir == 'down':
        return row + steps_, col
    if dir == 'left':
        return row, col - steps_
    if dir == 'right':
        return row, col + steps_


def inside(row_, col_, size_):
    return 0 <= row_ < size_ and 0 <= col_ < size_


size = 5

matrix = []

player_row = 0
player_col = 0
targets = 0

for row in range(size):
    elements = input().split()
    for col in range(size):
        if elements[col] == 'A':
            player_row = row
            player_col = col
        elif elements[col] == 'x':
            targets += 1
    matrix.append(elements)

matrix[player_row][player_col] = '.'

hit_targets = []
n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0]
    direction = command_parts[1]

    if command == 'move':
        steps = int(command_parts[2])
        next_row, next_col = get_next_steps(player_row, player_col, direction, steps)

        if inside(next_row, next_col, size) and matrix[next_row][next_col] == '.':
            player_row, player_col = next_row, next_col

    else:
        bullet_row, bullet_col = get_next_steps(player_row, player_col, direction, 1)

        while inside(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == 'x':
                targets -= 1
                matrix[bullet_row][bullet_col] = '.'
                hit_targets.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = get_next_steps(bullet_row, bullet_col, direction, 1)

        if targets == 0:
            break
if targets == 0:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f'Training not completed! {targets} targets left.')
print(*hit_targets, sep='\n')
