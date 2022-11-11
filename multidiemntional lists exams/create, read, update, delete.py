def move(direction, position_):
    if direction == 'up':
        position_[0] -= 1
    if direction == 'down':
        position_[0] += 1
    if direction == 'left':
        position_[1] -= 1
    if direction == 'right':
        position_[1] += 1
    return position_


size = 6

matrix = []

for _ in range(size):
    matrix.append(input().split())

position = list(map(int, input().strip('(').strip(')').split(', ')))

while True:

    line = input()
    command = line.split(', ')

    if line == 'Stop':
        break

    position = move(command[1], position)
    if command[0] == 'Create':
        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = command[2]
    elif command[0] == 'Update':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = command[2]
    elif command[0] == 'Delete':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = '.'
    elif command[0] == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])

for row in matrix:
    print(''.join(row))
