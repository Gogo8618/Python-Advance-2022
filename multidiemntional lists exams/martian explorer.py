def rover_positions(mx, row_, col_, deposit_):
    position = mx[row_][col_]
    if position in ['W', 'C', 'M']:
        print(f"{deposit_[position][0]} deposit found at ({row_}, {col_})")
        deposit_[position][1] += 1
    elif position == 'R':
        return 'broken'
    return deposit_


size = 6
if_is_broken = False
is_found = False
matrix = []
rover_row = 0
rover_col = 0
for row in range(size):
    element = input().split()
    for col in range(size):
        if element[col] == 'E':
            rover_row = row
            rover_col = col

    matrix.append(element)

deposit = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}
command = input().split(', ')

for c in command:
    if c == 'up':
        if rover_row > 0:
            rover_row -= 1
        else:
            rover_row = 5
    elif c == 'down':
        if rover_row < 5:
            rover_row += 1
        else:
            rover_row = 0
    elif c == 'left':
        if rover_col > 0:
            rover_col -= 1
        else:
            rover_col = 5
    elif c == 'right':
        if rover_col < 5:
            rover_col += 1
        else:
            rover_col = 0
    result = rover_positions(matrix, rover_row, rover_col, deposit)
    if result == 'broken':
        if_is_broken = True
        break
    deposit = result

if if_is_broken:
    print(f"Rover got broken at ({rover_row}, {rover_col})")
if deposit['W'][1] >= 1 and deposit['C'][1] >= 1 and deposit['M'][1] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
