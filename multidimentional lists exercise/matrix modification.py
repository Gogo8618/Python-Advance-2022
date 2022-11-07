n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:

    command = input()
    if command == "END":
        break
    current_command = command.split()

    row, col, value = [int(x) for x in current_command[1:]]

    if row < 0 or col < 0 or row >= n or col >= n:
        print("Invalid coordinates")
        continue

    if current_command[0] == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row)