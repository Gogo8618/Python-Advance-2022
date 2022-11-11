tom, jerry = input().split(', ')
size = 6
matrix = []

tom_need_to_rest = False
jerry_need_to_rest = False

for _ in range(size):
    matrix.append(input().split())

while True:
    tom_coordinates = input()
    if not tom_need_to_rest:
        row, col = map(int, tom_coordinates.strip('(').strip(')').split(', '))

        if matrix[row][col] == 'E':
            print(f"{tom} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            print(f"{tom} is out of the game! The winner is {jerry}.")
            break
        elif matrix[row][col] == 'W':
            print(f"{tom} hits a wall and needs to rest.")
            tom_need_to_rest = True
    else:
        tom_need_to_rest = False

    jerry_coordinates = input()
    if not jerry_need_to_rest:
        row, col = map(int, jerry_coordinates.strip('(').strip(')').split(', '))
        if matrix[row][col] == 'E':
            print(f"{jerry} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            print(f"{jerry} is out of the game! The winner is {tom}.")
            break
        elif matrix[row][col] == 'W':
            print(f"{jerry} hits a wall and needs to rest.")
            jerry_need_to_rest = True
    else:
        jerry_need_to_rest = False
