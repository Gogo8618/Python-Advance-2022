size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0
for row in range(size):
    element = input().split()
    for col in range(size):
        if element[col] == 'B':
            bunny_row = row
            bunny_col = col
    matrix.append(element)

directions = {'right': lambda r, c: (r, c + 1),
              'left': lambda r, c: (r, c - 1),
              'up': lambda r, c: (r - 1, c),
              'down': lambda r, c: (r + 1, c)}

for direction in directions:
    current_sum = 0

    row, col = directions[direction](bunny_row, bunny_col)
    while 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        current_sum += int(matrix[row][col])
        row, col = directions[direction](row, col)
