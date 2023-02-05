def deposit_or_rock(mx, pos, deposit):
    current_position = mx[pos[0]][pos[1]]
    if current_position in ['W', 'C', 'M']:
        print(f"{deposit[current_position][0]} deposit found at {pos[0], pos[1]}")
        deposit[current_position][1] += 1
    elif current_position == 'R':
        return 'broken'
    return deposit



matrix = []
deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0], }
position = []
is_broken = False
rover_position = False

for _ in range(6):
    matrix.append([x for x in input().split()])

for row in range(6):
    for col in range(6):
        if matrix[row][col] == 'E':
            position = [row, col]
            rover_position = True
            break
    if rover_position:
        break

command = input().split(', ')

for c in command:
    if c == 'up':
        if position[0] > 0:
            position[0] -= 1
        else:
            position[0] = 5
    elif c == 'down':
        if position[0] < 5:
            position[0] += 1
        else:
            position[0] = 0
    elif c == 'left':
        if position[1] > 0:
            position[1] -= 1
        else:
            position[1] = 5
    elif c == 'right':
        if position[1] < 5:
            position[1] += 1
        else:
            position[1] = 0
    result_after_check = deposit_or_rock(matrix, position, deposits)
    if result_after_check == 'broken':
        is_broken = True
        break
    deposits = result_after_check
if is_broken:
    print(f"Rover got broken at {position[0], position[1]}")
if deposits['M'][1] >= 1 and deposits['W'][1] >= 1 and deposits['C'][1] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
