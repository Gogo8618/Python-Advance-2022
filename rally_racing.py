def find_T(mx, size):
    for r in range(size):
        for c in range(size):
            if mx[r][c] == 'T':
                return r, c


def move_direction(direction, position):
    if direction == 'up':
        position[0] -= 1
    elif direction == 'down':
        position[0] += 1
    elif direction == 'left':
        position[1] -= 1
    elif direction == 'right':
        position[1] += 1
    return position


n = int(input())
number_car = input()

matrix = []

kilometers = 0

coordinates = [0, 0]

for _ in range(n):
    matrix.append([x for x in input().split()])

while True:

    command = input()

    if command == 'End':
        print(f"Racing car {number_car} DNF.")
        matrix[coordinates[0]][coordinates[1]] = 'C'
        break
    coordinates = move_direction(command, coordinates)

    if matrix[coordinates[0]][coordinates[1]] == 'F':
        kilometers += 10
        matrix[coordinates[0]][coordinates[1]] = 'C'
        print(f"Racing car {number_car} finished the stage!")
        break

    if matrix[coordinates[0]][coordinates[1]] == '.':
        kilometers += 10
    elif matrix[coordinates[0]][coordinates[1]] == 'T':
        kilometers += 30
        matrix[coordinates[0]][coordinates[1]] = '.'

        coordinates[0], coordinates[1] = find_T(matrix, n)
        matrix[coordinates[0]][coordinates[1]] = '.'
print(f"Distance covered {kilometers} km.")

for row in matrix:
    print(''.join(row))
