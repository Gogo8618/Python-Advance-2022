def move(direction, pos):
    if direction == 'up':
        pos[0] -= 1
    elif direction == 'down':
        pos[0] += 1
    elif direction == 'left':
        pos[1] -= 1
    elif direction == 'right':
        pos[1] += 1
    return position


matrix = []

for _ in range(6):
    matrix.append([x for x in input().split()])

position = list(map(int, input().strip('(').strip(')').split(', ')))

while True:
    command = input().split(', ')

    if command[0] == 'Stop':
        break
    position = move(command[1], position)

    if command[0] == 'Create':
        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = command[2]
    elif command[0] == 'Update':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = command[2]
    elif command[0] == 'Delete':
        if matrix[position[0]][position[1]].isalnum():
            matrix[position[0]][position[1]] = '.'
    elif command[0] == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])
for row in matrix:
    print(' '.join(row))
