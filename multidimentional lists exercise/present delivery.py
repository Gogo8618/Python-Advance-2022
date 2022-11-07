def get_next_steps(row_, col_, dir_):
    if dir_ == 'up':
        return row_ - 1, col_
    if dir_ == 'down':
        return row_ + 1, col_
    if dir_ == 'left':
        return row_, col_ - 1
    if dir_ == 'right':
        return row_, col_ + 1


def inside(row_, col_, size_):
    return 0 <= row_ < size_ and 0 <= col_ < size_


def gifted_around(matrix_, row_, col_):
    result = []
    if inside(row_, col_ - 1, len(matrix_)) and matrix_[row_][col_ - 1] == 'X' or matrix_[row_][col_ - 1] == 'V':
        result.append([row_, col_ - 1])
    if inside(row_, col + 1, len(matrix_)) and matrix_[row_][col_ + 1] == 'X' or matrix_[row_][col_ + 1] == 'V':
        result.append([row_, col_ + 1])
    if inside(row_ - 1, col_, len(matrix_)) and matrix_[row_ - 1][col_] == 'X' or matrix_[row_ - 1][col_] == 'V':
        result.append([row_ - 1, col_])
    if inside(row_ + 1, col, len(matrix_)) and matrix_[row_ + 1][col] == 'X' or matrix_[row_ + 1][col_] == 'V':
        result.append([row_ + 1, col])
    return result


matrix = []
presents = int(input())
size = int(input())

santa_row = 0
santa_col = 0
nice_kids = 0

gifted_kids = 0
for row in range(size):
    elements = input().split()
    for col in range(size):
        if elements[col] == 'S':
            santa_row = row
            santa_col = col
        elif elements[col] == 'V':
            nice_kids += 1
    matrix.append(elements)
while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_steps(santa_row, santa_col, command)
    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        gifted_kids += 1
    elif matrix[santa_row][santa_col] == 'C':
        around_santa = gifted_around(matrix, santa_row, santa_col)
        for kid_row, kid_col in around_santa:
            if matrix[kid_row][kid_col] == 'V':
                gifted_kids += 1
            presents -= 1
            matrix[kid_row][kid_col] = '-'
            if presents == 0:
                break
    matrix[santa_row][santa_col] = 'S'

if gifted_kids != nice_kids and presents == 0:
    print('Santa ran out of presents!')
for row in matrix:
    print(*row)
if gifted_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - gifted_kids} nice kid/s.")
