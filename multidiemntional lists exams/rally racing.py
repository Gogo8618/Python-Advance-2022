def find_exit(matrix_, size_):
    for r in range(size_):
        for c in range(size_):
            if matrix_[r][c] == 'T':
                return r, c


size = int(input())
car_number = input()

matrix = []
kilometers = 0
car_position = [0, 0]
for _ in range(size):
    matrix.append(input().split())

while True:
    line = input()

    if line == 'End':
        matrix[car_position[0]][car_position[1]] = 'C'
        print(f"Racing car {car_number} DNF.")
        break

    if line == 'up':
        car_position[0] -= 1
    elif line == 'down':
        car_position[0] += 1
    elif line == 'left':
        car_position[1] -= 1
    elif line == 'right':
        car_position[1] += 1

    if matrix[car_position[0]][car_position[1]] == 'F':
        kilometers += 10
        matrix[car_position[0]][car_position[1]] = 'C'
        print(f"Racing car {car_number} finished the stage!")
        break
    elif matrix[car_position[0]][car_position[1]] == 'T':
        kilometers += 30
        matrix[car_position[0]][car_position[1]] = '.'
        car_position[0], car_position[1] = find_exit(matrix, size)
        matrix[car_position[0]][car_position[1]] = '.'
    else:
        kilometers += 10
print(f"Distance covered {kilometers} km.")
for row in matrix:
    print(''.join(row))
